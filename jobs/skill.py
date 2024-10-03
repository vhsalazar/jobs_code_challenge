class Skill:
    _instances = {}

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __new__(cls, key, *args, **kwargs):
        """Multiton Pattern to ensure only one instance of a skill is created"""
        if key not in cls._instances:
            cls._instances[key] = super(Skill, cls).__new__(cls)
        return cls._instances[key]

    @classmethod
    def parse(cls, skills: str) -> list:
        """Parse a string of skills and return a list of Skill instances"""
        return [Skill(name) for name in skills.split(', ')]
