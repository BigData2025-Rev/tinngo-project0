import json
import csv
import os
import re
from dataclasses import asdict
from models.recipe import Recipe

class FileHandler:
    
    def __init__(self, save_file='./data/recipes.json'):
        self.save_file = save_file

    def save_json(self, recipe):
        with open(self.save_file, 'a', encoding='utf-8') as f:
            json.dump(asdict(recipe), f, indent=4)
            print("Saved recipe!")

    def is_csv(self, file_path):
        return os.path.isfile(file_path) and file_path.lower().endswith('.csv')

    def read_csv(self, file_path):
        if (not self.is_csv(file_path)):
            return None

        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                recipe = Recipe()

                recipe.name = row['name']
                recipe.prep_time = row['prep_time (in mins)']
                recipe.cook_time = row['cook_time (in mins)']

                recipe.instructions.append(row['instructions'])

                ingredients_quantity = row['ingredients_quantity']
                pattern = r'(\d+(\/\d+)?[^\d]*)'
                matches = re.finditer(pattern, ingredients_quantity)
                recipe.ingredients = [match.group().strip() for match in matches]

                yield recipe
        return recipe