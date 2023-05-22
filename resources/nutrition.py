import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

nutrition = Blueprint('nutrition', 'recipe')


@nutrition.route('/', methods=['GET'])
def nutrition_index():
    result = models.Nutrition.select()
    print('result of nutrition select query')
    print(result)

    nutrition_dicts = [model_to_dict(recipe) for recipe in result]
    
    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

@nutrition.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    recipe = models.Nutrition.get_by_id(id)
    print(recipe)
    return jsonify(
        data=model_to_dict(recipe),
        message="Success!!!",
        status=200
    ), 200


@nutrition.route('/', methods=['POST'])

def create_recipe():
    payload = request.get_json()
    print(payload)
    new_recipe = models.Nutrition.create(title=payload['title'], description=payload['description'], time=payload['time'])
    print(new_recipe) # just prints the ID -- check sqlite3 to see the data 

    nutrition_dict = model_to_dict(new_recipe)
    return jsonify(
        data=nutrition_dict,
        message="Sucessfully created a recipe!",
        status=201
    ), 201
