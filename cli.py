import sys

from jobs import *
from jobs.utils import read_csv

class CLI:
    HEADERS = ['job_seeker_id', 'job_seeker_name', 'job_id',
               'job_title', 'matching_skills', 'matching_skills_percent']

    @classmethod
    def call(cls, args):
        if len(args) != 3:
            print("Usage: python main.py <jobs.csv> <jobseekers.csv>")
            sys.exit(1)

        jobs_path = sys.argv[1]  # 'jobs.csv'
        job_seekers_path = sys.argv[2]  # 'jobseekers.csv'

        jobs = []
        for job_row in read_csv(jobs_path):
            required_skills = Skill.parse(job_row['required_skills'])
            job = Job(int(job_row['id']), job_row['title'], required_skills)
            jobs.append(job)

        job_seekers = []
        for job_seeker_row in read_csv('jobseekers.csv'):
            skill_list = Skill.parse(job_seeker_row['skills'])
            job_seeker = JobSeeker(
                int(job_seeker_row['id']), job_seeker_row['name'], skill_list)
            job_seekers.append(job_seeker)

        job_matcher = JobMatcher(job_seekers, jobs)

        # A new class could handle the output of the recomendations
        # however, for this simple case, we can just print the output        
        print(','.join(CLI.HEADERS))

        for recommendation in job_matcher.recommendations:
            print(recommendation)


if __name__ == '__main__':
    CLI.call(sys.argv)
