import sqlite3
import json
from models.recipe import Recipe

class DbHandler:
    def __init__(self, db_file_path="./data/recipes.db"):
        self.conn = sqlite3.connect(db_file_path)
        self.cursor = self.conn.cursor()
        self.__create_table()

    def __create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                prep_time TEXT,
                cook_time TEXT,
                ingredients TEXT,
                instructions TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, recipe):
        ing_str = json.dumps(recipe.ingredients)
        ins_str = json.dumps(recipe.instructions)
        self.cursor.execute('''
            INSERT INTO recipes VALUES (NULL, ?, ?, ?, ?, ?)
        ''', (recipe.name, recipe.prep_time, recipe.cook_time, ing_str, ins_str))
        self.conn.commit()
        print("Saved to db!")

    def retrieve_randomly(self):
        self.cursor.execute('SELECT * FROM recipes ORDER BY RANDOM() LIMIT 1')
        random_recipe = self.cursor.fetchone()
        if random_recipe:
            recipe = Recipe()
            recipe.name = random_recipe[1]
            recipe.prep_time = random_recipe[2]
            recipe.cook_time = random_recipe[3]
            recipe.ingredients = json.loads(random_recipe[4])
            recipe.instructions = json.loads(random_recipe[5])

            return recipe
        else:
            return None

    def __del__(self):
        self.conn.close()
