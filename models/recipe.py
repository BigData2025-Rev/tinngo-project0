from dataclasses import dataclass, field

@dataclass
class Recipe:
    name: str = ''
    ingredients: list[str] = field(default_factory=list)
    prep_time: str = ''
    cook_time: str = ''
    instructions: list[str] = field(default_factory=list)
