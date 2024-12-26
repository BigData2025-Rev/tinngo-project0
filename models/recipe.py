from dataclasses import dataclass, field

@dataclass
class Recipe:
    name: str = ''
    ingredients: list[str] = field(default_factory=list)
    prep_time: str = ''
    cook_time: str = ''
    instructions: list[str] = field(default_factory=list)

    def __repr__(self):
        ing_str = "\n".join(f"    {ingredient}" for ingredient in self.ingredients)
        ins_str = "\n".join(f"    {i+1}. {instruction}" for i, instruction in enumerate(self.instructions))
        return (
            f"Name: {self.name}\n"
            f"Prep Time: {self.prep_time}\n"
            f"Cook Time: {self.cook_time}\n"
            f"Ingredients: \n{ing_str}\n"
            f"Instructions: \n{ins_str}\n"
        )
