import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

desserts = Blueprint('desserts', 'desserts')

# GET all route
@desserts.route('/', methods=['GET'])
def nutrition_index():
    result = models.Desserts.select()
    print('result of nutrition select query')
    print(result)

    nutrition_dicts = [model_to_dict(recipe) for recipe in result]
    
    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

# GET route
@desserts.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    recipe = models.Desserts.get_by_id(id)
    print(recipe)
    return jsonify(
        data=model_to_dict(recipe),
        message="Success!!!",
        status=200
    ), 200


# POST route
@desserts.route('/', methods=['POST'])

def create_recipe():
    payload = request.get_json()
    print(payload)
    new_recipe = models.Desserts.create(title=payload['title'], img=payload['img'], time=payload["time"], ingredients=payload["ingredients"], description=payload['description'])
    print(new_recipe) # just prints the ID -- check sqlite3 to see the data 

    nutrition_dict = model_to_dict(new_recipe)
    return jsonify(
        data=nutrition_dict,
        message="Sucessfully created a recipe!",
        status=201
    ), 201

# PUT route
@desserts.route('/<id>', methods=['PUT'])
def update_recipe(id):
    payload = request.get_json()
    print(payload)
    
    models.Desserts.update(**payload).where(models.Desserts.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Desserts.get_by_id(id)),
        message="Recipe has been successfully updated!",
        status=200
    ),200


# DELETE route
@desserts.route('/<id>', methods=['DELETE'])
def delete_recipe(id):

    delete_query = models.Desserts.delete().where(models.Desserts.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} recipe with id {id}",
        status=200
    ), 200
