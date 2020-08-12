import requests
import json


def get_response_id(food):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "24b9f29661msh672b30c1f618a39p1a7cfejsnb3e7b672fb6e"
        }
    querystring = {"number":"10","offset":"0","query":food}
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed_response = json.loads(response.text)
    return parsed_response

def get_response_recipe(food_id):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "24b9f29661msh672b30c1f618a39p1a7cfejsnb3e7b672fb6e"
        }
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(food_id) + "/ingredientWidget.json"
    response = requests.request("GET", url, headers=headers)
    parsed_response = json.loads(response.text)
    return parsed_response


def recipe_options(parsed_response_id):
    recipe_list = []
    for i in range(0, len(parsed_response_id["results"])):
        recipe_list.append(str(parsed_response_id["results"][i]["title"]))
    return recipe_list


def food_id(chosen_recipe, parsed_response_id):
    food_id = parsed_response_id["results"][chosen_recipe]["id"]
    return food_id

def ingredients(parsed_response_recipe):

    ingredients = []

    for i in range(0, len(parsed_response_recipe["ingredients"])):
        name = parsed_response_recipe["ingredients"][i]["name"]
        value = parsed_response_recipe["ingredients"][i]["amount"]["us"]["value"]
        unit = parsed_response_recipe["ingredients"][i]["amount"]["us"]["unit"]
        # print(name + ": " + str(value) + " " + unit)

        ingredients.append(name)

    return ingredients

def recipe_photo(parsed_response_id):
    recipe_photos_list = []
    for i in range(0, len(parsed_response_id["results"])):
        recipe_photos_list.append(parsed_response_id["results"][i]["image"])
    return recipe_photos_list

def recipe_amount(parsed_response_recipe):
    recipe_amount_list = []
    for i in range(0, len(parsed_response_recipe["ingredients"])):
        recipe_amount_list.append(parsed_response_recipe["ingredients"][i]["amount"]["us"]["value"])
    return recipe_amount_list

def recipe_amount_unit(parsed_response_recipe):
    recipe_amount_unit_list = []
    for i in range(0, len(parsed_response_recipe["ingredients"])):
        recipe_amount_unit_list.append(parsed_response_recipe["ingredients"][i]["amount"]["us"]["unit"])
    return recipe_amount_unit_list



# needed to remove from global scope
if __name__ == "__main__":


    #runs enter_food() function
    food = input("\nEnter desired food: ")

    # parsed reponse, we want id
    parsed_response_id = get_response_id(food)

    print(parsed_response_id)

    # list of recipe options given parsed_response dict from entered food
    recipe_list = recipe_options(parsed_response_id)

    # list of recipe images given parsed_response dict from entered food
    recipe_photos_list = recipe_photo(parsed_response_id)

    # place holder for printed recipe number
    recipe_number = 0

    print("\nHere are your recipe options for your desired food, '" + food + "': \n")

    for recipe in recipe_list:
        recipe_number += 1
        print(str(recipe_number) + ". " + recipe)

    print("\n------------------------------------IMAGES------------------------------------\n")

    for recipe_photo in recipe_photos_list:
        print("https://spoonacular.com/recipeImages/" + recipe_photo)

    number = eval(input("Which recipe, enter number: "))

    # returns index of recipe in parsed_response_id
    # chosen_recipe = chosen_recipe(number)

    chosen_recipe = number - 1

    # id of chosen id
    food_id = food_id(chosen_recipe, parsed_response_id)

    # parsed response, when we want ingredients for particular id
    parsed_response_recipe = get_response_recipe(food_id)

    print("\nHere are the ingredients for", recipe_list[chosen_recipe], "\n")

    ingredients = ingredients(parsed_response_recipe)

    print(ingredients)



