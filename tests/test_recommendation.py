import unittest
from jobs import Job, JobSeeker, Recommendation

class TestRecommendation(unittest.TestCase):
    def setUp(self):
        self.job = Job(1, "Software Engineer", ["Python", "Django", "REST"])
        self.job_seeker = JobSeeker(1, "Alice", ["Python", "Django", "GraphQL"])
        self.recommendation = Recommendation(self.job, self.job_seeker)

    def test_matching_skill_count(self):
        self.assertEqual(self.recommendation.matching_skill_count, 2)

    def test_matching_skill_percent(self):
        self.assertEqual(self.recommendation.matching_skill_percent, 66)

    def test_str(self):
        expected_str = "1, Alice, 1, Software Engineer, 2, 66"
        self.assertEqual(str(self.recommendation), expected_str)

    def test_no_matching_skills(self):
        job_seeker = JobSeeker(2, "Bob", ["Java", "Spring"])
        recommendation = Recommendation(self.job, job_seeker)
        self.assertEqual(recommendation.matching_skill_count, 0)
        self.assertEqual(recommendation.matching_skill_percent, 0)

    def test_all_matching_skills(self):
        job_seeker = JobSeeker(3, "Charlie", ["Python", "Django", "REST"])
        recommendation = Recommendation(self.job, job_seeker)
        self.assertEqual(recommendation.matching_skill_count, 3)
        self.assertEqual(recommendation.matching_skill_percent, 100)

    def test_empty_required_skills(self):
        job = Job(2, "Data Scientist", [])
        job_seeker = JobSeeker(4, "Dana", ["Python", "Pandas"])
        recommendation = Recommendation(job, job_seeker)
        self.assertEqual(recommendation.matching_skill_count, 0)
        self.assertEqual(recommendation.matching_skill_percent, 0)