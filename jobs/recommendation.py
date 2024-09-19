class Recommendation:
    def __init__(self, job, job_seeker):
        self.job = job
        self.job_seeker = job_seeker

    @property
    def matching_skill_count(self):
        job_seeker_skills = set(self.job_seeker.skills)
        return len(self.job.required_skills.intersection(job_seeker_skills))

    @property
    def matching_skill_percent(self):
        return int(self.matching_skill_count / len(self.job.required_skills) * 100)

    def __str__(self) -> str:
        return ', '.join(map(str, [self.job_seeker.id, self.job_seeker.name, self.job.id, self.job.title, self.matching_skill_count, self.matching_skill_percent]))
