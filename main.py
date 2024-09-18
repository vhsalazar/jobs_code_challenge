import csv
from collections import defaultdict
from typing import List


def read_csv(file_path):
    with open(file_path, mode='r') as file:
        # reader = csv.reader(file, delimiter=',')
        reader = csv.DictReader(file)
        return [row for row in reader]


class Skill:
    _instances = {}

    def __init__(self, name: str):
        self.name = name
        self.jobs = []

    def __str__(self) -> str:
        return f"Skill: {self.name} - Jobs: {self.jobs}"

    def __repr__(self) -> str:
        return self.name

    def __new__(cls, key, *args, **kwargs):
        """Multiton Pattern to ensure only one instance of a skill is created"""
        if key not in cls._instances:
            cls._instances[key] = super(Skill, cls).__new__(cls)
        return cls._instances[key]

    @classmethod
    def parse(self, skills: str) -> list:
        """Parse a string of skills and return a list of Skill instances"""
        return [Skill(name) for name in skills.split(', ')]


class Job:
    def __init__(self, id: int, title: str, required_skills: List[Skill]):
        self.id = id
        self.title = title
        self.required_skills = required_skills
    
    def __repr__(self) -> str:
        return self.title


class JobSeeker:
    def __init__(self, id: int, name: str, skills: List[Skill]):
        self.id = id
        self.name = name
        self.skills = skills

    def __repr__(self) -> str:
        return self.name


class JobRecommendation:
    def __init__(self, job_seekers: List[JobSeeker], jobs: List[Job]):
        self.job_seekers = job_seekers
        self.jobs = jobs
        self.recommendations = []
        self.skill_jobs = defaultdict(list)

        for job in jobs:
            for skill in job.required_skills:
                self.skill_jobs[skill].append(job)

    def __str__(self) -> str:
        return f"Job: {self.job.title} - Job Seeker: {self.job_seeker.name} - Score: {self.score}"

    def calculate(self) -> list:
        result = []
        for job_seeker in self.job_seekers:
            job_seeker_skills = set(job_seeker.skills)
            jobs = [] 
            for skill in job_seeker_skills:
                jobs.extend(self.skill_jobs[skill])
            for job in jobs:
                matching_skill_count = len(set(job.required_skills).intersection(job_seeker_skills))
                matching_skill_percent = int(matching_skill_count / len(job.required_skills) * 100)
                result.append([job_seeker.id, job_seeker.name, job.id, job.title, matching_skill_count, matching_skill_percent])
        return result


skills = defaultdict(list)
jobs = []
for job_row in read_csv('jobs.csv'):    
    required_skills = Skill.parse(job_row['required_skills'])
    job = Job(int(job_row['id']), job_row['title'], required_skills)
    jobs.append(job)
    for skill in required_skills:
        skills[skill].append(job_row['id'])

job_seekers = []
for job_seeker_row in read_csv('jobseekers.csv'):
    skill_list = Skill.parse(job_seeker_row['skills'])
    job_seeker = JobSeeker(
        int(job_seeker_row['id']), job_seeker_row['name'], skill_list)
    job_seekers.append(job_seeker)


r = JobRecommendation(job_seekers, jobs)
r.calculate()