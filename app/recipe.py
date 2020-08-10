import requests
import json

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "24b9f29661msh672b30c1f618a39p1a7cfejsnb3e7b672fb6e"
    }

def get_response_id(url, headers, food):
    querystring = {"number":"10","offset":"0","query":food}
    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed_response = json.loads(response.text)
    return parsed_response

def get_response_recipe(url, headers, food_id):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(food_id) + "/ingredientWidget.json"
    response = requests.request("GET", url, headers=headers)
    parsed_response = json.loads(response.text)
    return parsed_response

def enter_food():
    food = input("\nEnter desired food: ")
    return food


def recipe_options(parsed_response_id):
    recipe_list = []
    for i in range(0, len(parsed_response_id["results"])):
        recipe_list.append(str(parsed_response_id["results"][i]["title"]))
    return recipe_list

def chosen_recipe(recipe_list):
    chosen_recipe = eval(input("\nWhich recipe do you want to add? (enter number): "))

    # adjust for position in index
    true_index_of_recipe = chosen_recipe - 1
    return true_index_of_recipe

def food_id(chosen_recipe, parsed_response_id):
    food_id = parsed_response_id["results"][chosen_recipe]["id"]
    return food_id

def ingredients(food_id, parsed_response_recipe):

    for i in range(0, len(parsed_response_recipe["ingredients"])):
        name = parsed_response_recipe["ingredients"][i]["name"]
        value = parsed_response_recipe["ingredients"][i]["amount"]["us"]["value"]
        unit = parsed_response_recipe["ingredients"][i]["amount"]["us"]["unit"]
        print(name + ": " + str(value) + " " + unit)


# needed to remove from global scope
if __name__ == "__main__":

    #runs enter_food() function
    food = enter_food()

    # parsed reponse, we want id
    parsed_response_id = get_response_id(url, headers, food)

    # list of recipe options given parsed_response dict from entered food

    recipe_list = recipe_options(parsed_response_id)

    # place holder for printed recipe number
    recipe_number = 0

    print("\nHere are your recipe options for your desired food, '" + food + "': \n")

    for recipe in recipe_list:
        recipe_number += 1
        print(str(recipe_number) + ". " + recipe)

    # returns index of recipe in parsed_response_id
    chosen_recipe = chosen_recipe(recipe_list)

    # id of chosen id
    food_id = food_id(chosen_recipe, parsed_response_id)

    # parsed response, when we want ingredients for particular id
    parsed_response_recipe = get_response_recipe(url, headers, food_id)

    print("\nHere are the ingredients for", recipe_list[chosen_recipe], "\n")

    ingredients = ingredients(food_id, parsed_response_recipe)




