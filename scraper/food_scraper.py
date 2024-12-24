import requests
from bs4 import BeautifulSoup
from models.recipe import Recipe

class FoodScraper:
    def __init__(self):
        self.recipe = None
        self.soup = None

    def run(self, url):
        self.recipe = Recipe()

        try:
            self.fetch_page(url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            return

        self.get_name()
        self.get_ingredients()
        self.get_time()
        self.get_instructions()

    def fetch_page(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:124.0) Gecko/20100101 Firefox/124.0'}
        response = requests.get(url, headers=headers, timeout=5)

        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def get_name(self):
        name_html = self.soup.find(class_='o-AssetTitle__a-HeadlineText')
        self.recipe.name = name_html.text.strip()

    def get_ingredients(self):
        ingredients_html = self.soup.find_all(class_='o-Ingredients__a-Ingredient--CheckboxLabel')
        for item in ingredients_html:
            ingredient = item.text.strip()
            if ingredient == "Deselect All":
                continue
            self.recipe.ingredients.append(ingredient)


    def get_time(self):
        time_html = self.soup.find(class_='o-RecipeInfo__m-Time')

        for li in time_html.find_all('li'):
            headline = li.find(class_='o-RecipeInfo__a-Headline')
            description = li.find(class_='o-RecipeInfo__a-Description')

            if headline and description:
                headline_text = headline.text.strip()
                description_text = description.text.strip()

                if 'Prep' in headline_text:
                    self.recipe.prep_time = description_text
                elif 'Cook' in headline_text:
                    self.recipe.cook_time = description_text

    def get_instructions(self):
        steps_html = self.soup.find_all(class_='o-Method__m-Step')
        for item in steps_html:
            step = item.text.strip()
            self.recipe.instructions.append(step)
