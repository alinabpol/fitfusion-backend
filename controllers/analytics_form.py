import models.nutrition_models as nutrition_models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

analytics_form = Blueprint('analytics_form', 'form')

# GET all route
@analytics_form.route('/', methods=['GET'])
def form_index():
    result = nutrition_models.Analytics.select()
    print('result of analytics_form select query')
    print(result)

    form_dicts = [model_to_dict(form) for form in result]
    
    return jsonify({
        'data': form_dicts,
        'message': f"Successfully found {len(form_dicts)} forms",
        'status': 200
    }), 200

# GET route
@analytics_form.route('/<id>', methods=['GET'])
def get_one_form(id):
    form = nutrition_models.Analytics.get_by_id(id)
    print(form)
    return jsonify(
        data=model_to_dict(form),
        message="Success!!!",
        status=200
    ), 200


# POST route
@analytics_form.route('/', methods=['POST'])

def create_form():
    payload = request.get_json()
    print(payload)
    new_form = nutrition_models.Analytics.create(activity=payload['activity'], time=payload['time'])
    print(new_form) # just prints the ID -- check sqlite3 to see the data 

    form_dict = model_to_dict(new_form)
    return jsonify(
        data=form_dict,
        message="Sucessfully created a form!",
        status=201
    ), 201

# PUT route
@analytics_form.route('/<id>', methods=['PUT'])
def update_form(id):
    payload = request.get_json()
    print(payload)
    
    nutrition_models.Analytics.update(**payload).where(nutrition_models.Analytics.id == id).execute()

    return jsonify(
        data=model_to_dict(nutrition_models.Analytics.get_by_id(id)),
        message="Form has been successfully updated!",
        status=200
    ),200


# DELETE route
@analytics_form.route('/<id>', methods=['DELETE'])
def delete_form(id):

    delete_query = nutrition_models.Analytics.delete().where(nutrition_models.Analytics.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data={},
        message=f"Successfully deleted {nums_of_rows_deleted} form with id {id}",
        status=200
    ), 200
