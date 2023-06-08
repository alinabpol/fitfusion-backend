import models.nutrition_models as nutrition_models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

workout = Blueprint('workout', 'workout')

# GET all route
@workout.route('/', methods=['GET'])
def workout_index():
    result = nutrition_models.Workout.select()
    print('result of workout select query')
    print(result)

    workout_dicts = [model_to_dict(training) for training in result]
    
    return jsonify({
        'data': workout_dicts,
        'message': f"Successfully found {len(workout_dicts)} workouts",
        'status': 200
    }), 200

# GET route
@workout.route('/<id>', methods=['GET'])
def get_one_workout(id):
    workout = nutrition_models.Workout.get_by_id(id)
    print(workout)
    return jsonify(
        data=model_to_dict(workout),
        message="Success!!!",
        status=200
    ), 200


# POST route
@workout.route('/', methods=['POST'])

def create_training():
    payload = request.get_json()
    print(payload)
    new_workout = nutrition_models.Workout.create(activity=payload['activity'], time=payload['time'], calories=payload['calories'], link=payload['link'])
    print(new_workout) 

    workout_dict = model_to_dict(new_workout)
    return jsonify(
        data=workout_dict,
        message="Sucessfully created a workout!",
        status=201
    ), 201

# PUT route
@workout.route('/<id>', methods=['PUT'])
def update_workout(id):
    payload = request.get_json()
    print(payload)
    
    nutrition_models.Workout.update(**payload).where(nutrition_models.Workout.id == id).execute()

    return jsonify(
        data=model_to_dict(nutrition_models.Workout.get_by_id(id)),
        message="Workout has been successfully updated!",
        status=200
    ),200


# DELETE route
@workout.route('/<id>', methods=['DELETE'])
def delete_workout(id):

    delete_query = nutrition_models.Workout.delete().where(nutrition_models.Workout.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} workout with id {id}",
        status=200
    ), 200