from flask import Blueprint, jsonify, request
from models.analytics_model import Analytics, collection
from bson import ObjectId


analytics = Blueprint('analytics', 'analytics')


# GET all route
@analytics.route('/', methods=['GET'])
def analytics_index():
    result = collection.find()
    print(result)
    analytics_dicts =  [
        # convert the ObjectId to a string
        {**analytics, '_id': str(analytics['_id'])} for analytics in result
    ]

    return jsonify({
        'data': analytics_dicts,
        'message': f"Successfully found {len(analytics_dicts)} forms",
        'status': 200
    }), 200

#GET route
@analytics.route('/<id>', methods=['GET'])
def get_one_form(id):
    analytics = collection.find_one({'_id': ObjectId(id)})
    if analytics:

        analytics['_id'] = str(analytics['_id'])

        return jsonify({
            'data': analytics,
            'message': 'Success!',
            'status': 200
        }), 200
    else:
        return jsonify({
            'data': {},
            'message': 'Form not found',
            'status': 404
        }), 404

# POST route
@analytics.route('/', methods=['POST'])
def create_form():
    payload = request.get_json()
    analytics = Analytics(**payload)
    result = analytics.save()
    if result:
        return jsonify({
            'data': analytics.__dict__,
            'message': 'Successfully created a form!',
            'status': 201
        }), 201
    else:
        return jsonify({
            'data': {},
            'message': 'Failed to create a form',
            'status': 400
        }), 400
    
# PUT route
@analytics.route('/<id>', methods=['PUT'])
def update_form(id):
    payload = request.get_json()
    print(payload)

    data = {
        'activity': payload['activity'],
        'time': int(payload['time']),
    }

    collection.update_one({'_id': ObjectId(id)}, {'$set': data})

    updated_form = collection.find_one({'_id': ObjectId(id)})
    updated_form['_id'] = str(updated_form['_id'])
    
    return jsonify(
        data=updated_form,
        message="Form has been successfully updated!",
        status=200
        ), 200


# DELETE route
@analytics.route('/<id>', methods=['DELETE'])
def delete_form(id):

    delete_query = collection.delete_one({'_id': ObjectId(id)})
    nums_of_rows_deleted = delete_query.deleted_count


    return jsonify(
        data={},
        message=f"Successfully deleted #{nums_of_rows_deleted} form with id {id}",
        status=200
    ), 200
