import unittest
from jobs import Skill

class TestSkill(unittest.TestCase):

    def test_singleton_pattern(self):
        skill1 = Skill("Python")
        skill2 = Skill("Python")
        self.assertIs(skill1, skill2, "Skill instances with the same name should be the same instance")

    def test_different_instances(self):
        skill1 = Skill("Python")
        skill2 = Skill("Java")
        self.assertIsNot(skill1, skill2, "Skill instances with different names should be different instances")

    def test_repr(self):
        skill = Skill("Python")
        self.assertEqual(repr(skill), "Python", "The __repr__ method should return the skill name")

    def test_parse(self):
        skills_str = "Python, Java, C++"
        skills = Skill.parse(skills_str)
        self.assertEqual(len(skills), 3, "There should be three skills parsed")
        self.assertEqual(repr(skills[0]), "Python", "The first skill should be 'Python'")
        self.assertEqual(repr(skills[1]), "Java", "The second skill should be 'Java'")
        self.assertEqual(repr(skills[2]), "C++", "The third skill should be 'C++'")

if __name__ == '__main__':
    unittest.main()