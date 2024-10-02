
from typing import List
from collections import defaultdict

from .skill import Skill
from .job_seeker import JobSeeker
from .job import Job
from .recommendation import Recommendation


class JobMatcher:
    """JobMatcher class to match job seekers with jobs based on their skills

    @param job_seekers: List of JobSeeker instances
    @param jobs: List of Job instances
    @param sort_by: Optional sort function to sort the recommendations
    """

    def __init__(self, job_seekers: List[JobSeeker], jobs: List[Job], sort_by=None):
        self.job_seekers = job_seekers
        self.jobs = jobs
        self.skill_jobs = defaultdict(list)
        self.sort_by = sort_by or self.__default_sort_by

        for job in jobs:
            for skill in job.required_skills:
                self.skill_jobs[skill].append(job)

    def __default_sort_by(self, recommendation: Recommendation) -> tuple:
        return (recommendation.job_seeker.id, -recommendation.matching_skill_percent, recommendation.job.id)

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
        return sorted(result, key=self.sort_by)
