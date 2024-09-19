from typing import List

from .skill import Skill


class JobSeeker:
    def __init__(self, id: int, name: str, skills: List[Skill]):
        self.id = id
        self.name = name
        self.skills = skills

    def __repr__(self) -> str:
        return self.name
