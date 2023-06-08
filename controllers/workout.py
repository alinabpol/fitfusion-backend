from flask import Blueprint, jsonify, request
from models.workout_model import Workout, collection
from bson.objectid import ObjectId


workout = Blueprint('workout', 'workout')


# GET all route
@workout.route('/', methods=['GET'])
def workout_index():
    result = collection.find()
    print(result)
    workout_dicts =  [
        # convert the ObjectId to a string
        {**workout, '_id': str(workout['_id'])} for workout in result
    ]

    return jsonify({
        'data': workout_dicts,
        'message': f"Successfully found {len(workout_dicts)} workouts",
        'status': 200
    }), 200

#GET route
@workout.route('/<id>', methods=['GET'])
def get_one_form(id):
    workout = collection.find_one({'_id': ObjectId(id)})
    if workout:

        workout['_id'] = str(workout['_id'])

        return jsonify({
            'data': workout,
            'message': 'Success!',
            'status': 200
        }), 200
    else:
        return jsonify({
            'data': {},
            'message': 'wWrkout not found',
            'status': 404
        }), 404

# POST route
@workout.route('/', methods=['POST'])
def create_form():
    payload = request.get_json()
    workout = Workout(**payload)
    result = workout.save()
    if result:
        return jsonify({
            'data': workout.__dict__,
            'message': 'Successfully created a workout!',
            'status': 201
        }), 201
    else:
        return jsonify({
            'data': {},
            'message': 'Failed to create a workout',
            'status': 400
        }), 400
    
# PUT route
@workout.route('/<id>', methods=['PUT'])
def update_form(id):
    payload = request.get_json()
    print(payload)

    data = {
        'activity': payload['activity'],
        'time': int(payload['time']),
        'calories': int(payload['calories']),
        'link': (payload['link']),

    }

    collection.update_one({'_id': ObjectId(id)}, {'$set': data})

    updated_form = collection.find_one({'_id': ObjectId(id)})
    updated_form['_id'] = str(updated_form['_id'])
    
    return jsonify(
        data=updated_form,
        message="wWorkout has been successfully updated!",
        status=200
        ), 200


# DELETE route
@workout.route('/<id>', methods=['DELETE'])
def delete_form(id):

    delete_query = collection.delete_one({'_id': ObjectId(id)})
    nums_of_rows_deleted = delete_query.deleted_count


    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} workout with id {id}",
        status=200
    ), 200
