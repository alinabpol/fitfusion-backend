from flask import Blueprint, jsonify, request
from models.nutrition_models import Lunch, lunch_collection
from bson.objectid import ObjectId


lunch = Blueprint('lunch', 'lunch')
collection = lunch_collection

# GET all route
@lunch.route('/', methods=['GET'])
def nutrition_index():
    result = collection.find()
    print(result)
    nutrition_dicts =  [
        # convert the ObjectId to a string
        {**lunch, '_id': str(lunch['_id'])} for lunch in result
    ]

    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

#GET route
@lunch.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    lunch = collection.find_one({'_id': ObjectId(id)})
    if lunch:

        lunch['_id'] = str(lunch['_id'])

        return jsonify({
            'data': lunch,
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
@lunch.route('/', methods=['POST'])
def create_recipe():
    payload = request.get_json()
    lunch = Lunch(**payload)
    result = lunch.save()
    if result:
        return jsonify({
            'data': lunch.__dict__,
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
@lunch.route('/<id>', methods=['PUT'])
def update_recipe(id):
    payload = request.get_json()
    print(payload)

    data = {
        'title': payload['title'],
        'img': payload['img'],
        'time': int(payload['time']),
        'ingredients': payload['ingredients'],
        'description': payload['description']
    }

    collection.update_one({'_id': ObjectId(id)}, {'$set': data})

    updated_recipe = collection.find_one({'_id': ObjectId(id)})
    updated_recipe['_id'] = str(updated_recipe['_id'])
    
    return jsonify(
        data=updated_recipe,
        message="Recipe has been successfully updated!",
        status=200
        ), 200


# DELETE route
@lunch.route('/<id>', methods=['DELETE'])
def delete_recipe(id):

    delete_query = collection.delete_one({'_id': ObjectId(id)})
    nums_of_rows_deleted = delete_query.deleted_count

    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} recipe with id {id}",
        status=200
    ), 200
