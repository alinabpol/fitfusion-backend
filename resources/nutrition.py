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


