from flask import Blueprint, jsonify, request
from models.nutrition_models import Breakfast, breakfast_collection
from bson import ObjectId


breakfast = Blueprint('breakfast', 'breakfast')

# GET all route
@breakfast.route('/', methods=['GET'])
def nutrition_index():
    result = breakfast_collection.find()
    print(result)
    nutrition_dicts =  [
        # convert the ObjectId to a string
        {**breakfast, '_id': str(breakfast['_id'])} for breakfast in result
    ]

    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

#GET route
@breakfast.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    breakfast = Breakfast.get_one(id)
    if breakfast:

        breakfast['_id'] = str(breakfast['_id'])

        return jsonify({
            'data': breakfast,
            'message': 'Success!',
            'status': 200
        }), 200
    else:
        return jsonify({
            'data': {},
            'message': 'Recipe not found',
            'status': 404
        }), 404

# POST route
@breakfast.route('/', methods=['POST'])
def create_recipe():
    payload = request.get_json()
    breakfast = Breakfast(**payload)
    result = breakfast.save()
    if result:
        return jsonify({
            'data': breakfast.__dict__,
            'message': 'Successfully created a recipe!',
            'status': 201
        }), 201
    else:
        return jsonify({
            'data': {},
            'message': 'Failed to create a recipe',
            'status': 400
        }), 400
    
# PUT route
@breakfast.route('/<id>', methods=['PUT'])
def update_recipe(id):
    payload = request.get_json()
    print(payload)

    updated_data = {
        'title': payload['title'],
        'img': payload['img'],
        'time': int(payload['time']),
        'ingredients': payload['ingredients'],
        'description': payload['description']
    }

    result = Breakfast.update(id, updated_data)

    updated_recipe = Breakfast.get_one(id)
    updated_recipe['_id'] = str(updated_recipe['_id'])
    return jsonify(
        data=updated_recipe,
        message="Recipe has been successfully updated!",
        status=200
        ), 200


# DELETE route
@breakfast.route('/<id>', methods=['DELETE'])
def delete_recipe(id):

    nums_of_rows_deleted = Breakfast.delete(id)

    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} recipe with id {id}",
        status=200
    ), 200
