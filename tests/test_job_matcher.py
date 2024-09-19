import unittest
from collections import namedtuple
from jobs import Skill, Job, JobMatcher, Recommendation, JobSeeker

class TestJobMatcher(unittest.TestCase):
    def setUp(self):
        self.skill_python = Skill("Python")
        self.skill_java = Skill("Java")
        self.skill_js = Skill("JavaScript")

        self.job_seeker_1 = JobSeeker(1, 'Alice', [self.skill_python, self.skill_java])
        self.job_seeker_2 = JobSeeker(2, 'Johana',[self.skill_js])
        
        self.job_1 = Job(1, 'Python Developer', [self.skill_python])
        self.job_2 = Job(2, 'Java Developer', [self.skill_java, self.skill_js])
        self.job_3 = Job(3, 'JS Developer', [self.skill_js])

        self.job_matcher = JobMatcher(
            [self.job_seeker_1, self.job_seeker_2],
            [self.job_1, self.job_2, self.job_3]
        )

    def test_recommendations(self):
        recommendations = self.job_matcher.recommendations

        # Check the number of recommendations
        self.assertEqual(len(recommendations), 4)
        
        # Check the recommendations
        self.assertEqual(recommendations[0].job_seeker.id, 1)
        self.assertEqual(recommendations[0].job.title, 'Python Developer')
        self.assertEqual(recommendations[0].matching_skill_count, 1)
        self.assertEqual(recommendations[0].matching_skill_percent, 100)
        
        self.assertEqual(recommendations[1].job_seeker.id, 1)
        self.assertEqual(recommendations[1].job.title, 'Java Developer')
        self.assertEqual(recommendations[1].matching_skill_count, 1)
        self.assertEqual(recommendations[1].matching_skill_percent, 50)
        
        
        self.assertEqual(recommendations[2].job_seeker.id, 2)
        self.assertEqual(recommendations[2].job.title, 'JS Developer')
        self.assertEqual(recommendations[2].matching_skill_count, 1)
        self.assertEqual(recommendations[2].matching_skill_percent, 100)
        
        self.assertEqual(recommendations[3].job_seeker.id, 2)
        self.assertEqual(recommendations[3].job.title, 'Java Developer')
        self.assertEqual(recommendations[3].matching_skill_count, 1)
        self.assertEqual(recommendations[3].matching_skill_percent, 50)