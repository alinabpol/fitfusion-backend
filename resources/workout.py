import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

workout = Blueprint('workout', 'training')

# GET all route
@workout.route('/', methods=['GET'])
def workout_index():
    result = models.Workout.select()
    print('result of workout select query')
    print(result)

    nutrition_dicts = [model_to_dict(training) for training in result]
    
    return jsonify({
        'data': nutrition_dicts,
        'message': f"Successfully found {len(nutrition_dicts)} workouts",
        'status': 200
    }), 200

# GET route
@workout.route('/<id>', methods=['GET'])
def get_one_recipe(id):
    training = models.Workout.get_by_id(id)
    print(training)
    return jsonify(
        data=model_to_dict(training),
        message="Success!!!",
        status=200
    ), 200


# POST route
@workout.route('/', methods=['POST'])

def create_training():
    payload = request.get_json()
    print(payload)
    new_training = models.Workout.create(activity=payload['activity'], time=payload['time'], calories=payload['calories'])
    print(new_training) # just prints the ID -- check sqlite3 to see the data 

    workout_dict = model_to_dict(new_training)
    return jsonify(
        data=workout_dict,
        message="Sucessfully created a workout!",
        status=201
    ), 201

# PUT route
@workout.route('/<id>', methods=['PUT'])
def update_training(id):
    payload = request.get_json()
    print(payload)
    
    models.Workout.update(**payload).where(models.Workout.id == id).execute()

    return jsonify(
        data=model_to_dict(models.Workout.get_by_id(id)),
        message="Workout has been successfully updated!",
        status=200
    ),200


# DELETE route
@workout.route('/<id>', methods=['DELETE'])
def delete_workout(id):

    delete_query = models.Workout.delete().where(models.Workout.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} workout with id {id}",
        status=200
    ), 200
