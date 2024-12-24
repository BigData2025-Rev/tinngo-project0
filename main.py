import json
from dataclasses import asdict
from scraper.food_scraper import FoodScraper


if __name__ == "__main__":
    scraper = FoodScraper()

    scraper.run("https://www.foodnetwork.com/recipes/alton-brown/southern-biscuits-recipe-2041990")

    with open("data/recipes.json", 'a', encoding='utf-8') as f:
        json.dump(asdict(scraper.recipe), f, indent=4)
