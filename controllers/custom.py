from flask import Blueprint, jsonify, request
from models.nutrition_models import Custom, custom_collection
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
import os


custom = Blueprint('custom', 'custom')
collection = custom_collection



# GET all route
@custom.route('/', methods=['GET'])
def nutrition_index():
    result = collection.find()
    print(result)
    nutrition_dicts =  [
        # convert the ObjectId to a string
        {**custom, '_id': str(custom['_id'])} for custom in result
    ]

    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

#GET route
@custom.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    custom = collection.find_one({'_id': ObjectId(id)})
    if custom:

        custom['_id'] = str(custom['_id'])

        return jsonify({
            'data': custom,
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

# PUT route
@custom.route('/<id>', methods=['PUT'])
def update_recipe(id):
    payload = request.get_json()
    print(payload)

    data = {
        'title': payload['title'],
        'img': payload['img'],
        'time': int(payload['time']),
        'ingredients': payload['ingredients'],
        'description': payload['description'],
        'file': payload['file']
    }
    if any(value is None for value in data.values()):
        return jsonify(message="Missing required fields", status=400), 400

    collection.update_one({'_id': ObjectId(id)}, {'$set': data})

    updated_recipe = collection.find_one({'_id': ObjectId(id)})
    updated_recipe['_id'] = str(updated_recipe['_id'])
    
    return jsonify(
        data=updated_recipe,
        message="Recipe has been successfully updated!",
        status=200
        ), 200


# DELETE route
@custom.route('/<id>', methods=['DELETE'])
def delete_recipe(id):

    delete_query = collection.delete_one({'_id': ObjectId(id)})
    nums_of_rows_deleted = delete_query.deleted_count

    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} recipe with id {id}",
        status=200
    ), 200
