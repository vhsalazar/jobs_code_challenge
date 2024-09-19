
from typing import List
from collections import defaultdict

from .skill import Skill
from .job_seeker import JobSeeker
from .job import Job
from .recommendation import Recommendation


class JobMatcher:
    def __init__(self, job_seekers: List[JobSeeker], jobs: List[Job]):
        self.job_seekers = job_seekers
        self.jobs = jobs
        self.skill_jobs = defaultdict(list)

        for job in jobs:
            for skill in job.required_skills:
                self.skill_jobs[skill].append(job)

    @property
    def recommendations(self) -> list:
        result = []
        for job_seeker in self.job_seekers:
            job_seeker_skills = set(job_seeker.skills)
            jobs = set()

            for skill in job_seeker_skills:
                for job in self.skill_jobs[skill]:
                    jobs.add(job)

            for job in jobs:
                result.append(Recommendation(job, job_seeker))
        return sorted(result, key=lambda r: (r.job_seeker.id, -r.matching_skill_percent, r.job.id))
