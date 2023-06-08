from flask import Blueprint, jsonify, request
from models.nutrition_models import Desserts, desserts_collection
from bson.objectid import ObjectId


desserts = Blueprint('desserts', 'desserts')
collection = desserts_collection

# GET all route
@desserts.route('/', methods=['GET'])
def nutrition_index():
    result = collection.find()
    print(result)
    nutrition_dicts =  [
        # convert the ObjectId to a string
        {**desserts, '_id': str(desserts['_id'])} for desserts in result
    ]

    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} recipes",
        'status': 200
    }), 200

#GET route
@desserts.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    desserts = collection.find_one({'_id': ObjectId(id)})
    if desserts:

        desserts['_id'] = str(desserts['_id'])

        return jsonify({
            'data': desserts,
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
@desserts.route('/', methods=['POST'])
def create_recipe():
    payload = request.get_json()
    desserts = Desserts(**payload)
    result = desserts.save()
    if result:
        return jsonify({
            'data': desserts.__dict__,
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
@desserts.route('/<id>', methods=['PUT'])
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
@desserts.route('/<id>', methods=['DELETE'])
def delete_recipe(id):

    delete_query = collection.delete_one({'_id': ObjectId(id)})
    nums_of_rows_deleted = delete_query.deleted_count

    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} recipe with id {id}",
        status=200
    ), 200
