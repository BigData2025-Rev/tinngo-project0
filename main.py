from scraper.food_scraper import FoodScraper
from db.file_handler import FileHandler
from db.db_handler import DbHandler

if __name__ == "__main__":
    scraper = FoodScraper()
    file_handler = FileHandler()
    db_handler = DbHandler()

    print("Welcome to the Recipe Data Scraper!")
    print("You can provide:")
    
    running = True
    while (running):
        print("[1] Url to a food website")
        print("[2] Path to local CSV file")
        print("[3] Get a random recipe from Db")
        print("[4] Exit")
        choice = input("")

        if (choice == "1"):
            # https://www.foodnetwork.com/recipes/alton-brown/southern-biscuits-recipe-2041990
            url = input("Please enter a FoodNetwork url: ")
            recipe = scraper.run(url)

            if (recipe is not None):
                print("Successful, this is the scraped recipe:")
                print(recipe)
                file_handler.save_json(recipe)
                db_handler.insert(recipe)

            else:
                print("Unsuccessful, please check URL")

        elif (choice == "2"):
            path = input("Please enter CSV file path: ")
            valid = file_handler.is_csv(path)

            if (valid):
                recipe_gen = file_handler.read_csv(path)
                for recipe in recipe_gen:

                    print(recipe)
                    file_handler.save_json(recipe)
                    db_handler.insert(recipe)

                    cont = input("Continue (Y/N): ").lower() == "y"
                    if (not cont):
                        break
                          
            else:
                print("Unsuccessful, please check file path")

        elif (choice == "3"):
            random_recipe = db_handler.retrieve_randomly()
            if (random_recipe):
                print(random_recipe)
            else:
                print("Database is empty!")

        elif (choice == "4"):
            break

        else:
            print("Unknown option, please choose again!")

        print("\n")
