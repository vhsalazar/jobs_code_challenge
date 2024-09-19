import unittest
from jobs.job_seeker import JobSeeker, Skill

class TestJobSeeker(unittest.TestCase):
    def setUp(self):
        self.skill1 = Skill("Python")
        self.skill2 = Skill("Django")
        self.skill3 = Skill("JavaScript")
        self.skills = [self.skill1, self.skill2, self.skill3]
        self.job_seeker = JobSeeker(1, 'Alice', self.skills)

    def test_job_seeker_initialization(self):
        self.assertEqual(self.job_seeker.id, 1)
        self.assertEqual(self.job_seeker.name, 'Alice')
        self.assertEqual(self.job_seeker.skills, set(self.skills))