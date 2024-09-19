from typing import List
from .skill import Skill

class Job:
    def __init__(self, id: int, title: str, required_skills: List[Skill]):
        self.id = id
        self.title = title
        self.required_skills = set(required_skills)

    def __repr__(self) -> str:
        return self.title