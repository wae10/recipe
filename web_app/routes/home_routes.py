from flask import Blueprint, render_template, redirect, request, flash

from app.recipe import get_response_id, get_response_recipe, recipe_options, food_id, ingredients, recipe_photo, recipe_amount, recipe_amount_unit

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    print(foods)
    #return "Welcome Home (TODO)"
    foods.clear()
    return render_template("home.html")

foods = []

@home_routes.route("/recipes", methods=["POST"])
def view_recipes():
    print("VISITED RECIPE PAGE") 
    print(foods)

    food = request.form["food"]
    foods.append(food)
    parsed_response_id = get_response_id(food)
    recipe_list = recipe_options(parsed_response_id)
    list_length = len(recipe_list)

    recipe_photos_list = recipe_photo(parsed_response_id)

    print(recipe_list)

    print(recipe_photos_list)

    return render_template("view_recipes.html", food = food, list_length = list_length, recipe_list = recipe_list, recipe_photos_list = recipe_photos_list)

@home_routes.route("/recipes/ingredients", methods=["POST"])
def view_ingredients():
    print("VISITED INGREDIENTS PAGE")
    print(foods)

    number = request.form["recipe"]

    number = eval(number)
    # get last element in the list
    parsed_response_id = get_response_id(foods[-1])

    recipe_list = recipe_options(parsed_response_id)

    true_index_of_recipe = number - 1

    food = food_id(true_index_of_recipe, parsed_response_id)

    parsed_response_recipe = get_response_recipe(food)

    recipe = recipe_list[true_index_of_recipe]

    ingredient = ingredients(parsed_response_recipe)

    recipe_amount_list = recipe_amount(parsed_response_recipe)

    recipe_amount_unit_list = recipe_amount_unit(parsed_response_recipe)

    return render_template("view_ingredients.html", ingredient = ingredient, recipe = recipe, recipe_amount_list = recipe_amount_list, recipe_amount_unit_list = recipe_amount_unit_list)