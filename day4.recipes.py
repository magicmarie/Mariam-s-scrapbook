fav_foods = {"noodles_list": ["add hot water to noodles in a bowl and cover it",
                              "wait for 3_4 minutes", "pour out the water",
                              "add spices/tomatoes/avocado as you wish"],
             "chapatis_list": ["mix flour, salt, onions together",
                               "add warm water to this mixture",
                               "frying"]}


def get_procedure(food_name):
    if food_name.lower() == "noodles":
        return fav_foods["noodles_list"]
    elif food_name.lower() == "chapatis":
        return fav_foods["chapatis_list"]
    else:
        return "am lost"


print(get_procedure("chapatis"))

ingredients = {"noodles_ingredients": ["noodles", "avocado", "tomatoes"],
               "chapatis_ingredients": ["baking flour", "salt", "onions"]}


def get_ingredient(ingredient):
    if ingredient.lower() == "noodles_ingredients":
        return ingredients["noodles_ingredients"]
    elif ingredient.lower() == "chapatis_ingredients":
        return ingredients["chapatis_ingredients"]
    else:
        return "doesnt exist"


print(get_ingredient("noodles_ingredients"))
