import unittest
from jobs.job import Job
from jobs.skill import Skill

class TestJob(unittest.TestCase):
    def setUp(self):
        self.skill1 = Skill("Python")
        self.skill2 = Skill("Django")
        self.skill3 = Skill("JavaScript")
        self.job = Job(1, "Backend Developer", [self.skill1, self.skill2])

    def test_job_initialization(self):
        self.assertEqual(self.job.id, 1)
        self.assertEqual(self.job.title, "Backend Developer")
        self.assertEqual(self.job.required_skills, {self.skill1, self.skill2})