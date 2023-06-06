from flask import Blueprint, jsonify, request
from models import Breakfast

breakfast = Blueprint('breakfast', 'breakfast')

# GET all route
@breakfast.route('/', methods=['GET'])
def nutrition_index():
    breakfasts = Breakfast.get_all()

    nutrition_dicts = [breakfast.__dict__ for breakfast in breakfasts]

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
        # Convert the ObjectId to a string
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

