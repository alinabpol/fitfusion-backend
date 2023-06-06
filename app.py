
from flask import Flask, g
from flask_cors import CORS
import pymongo

from pymongo import MongoClient


DEBUG = True
PORT = 8000

connection_url = 'mongodb+srv://admin:abcd1234@sei.cfwutib.mongodb.net/fitfusion?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

import models

from resources.breakfast import breakfast
# from resources.lunch import lunch
# from resources.dinner import dinner
# from resources.snacks import snacks
# from resources.smoothies import smoothies
# from resources.desserts import desserts
# from resources.analytics_form import analytics_form
# from resources.workout import workout
# from resources.chat import chat


# Database
DATABASE = client.get_database('fitfusion')



@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db_mongo = client.get_database('fitfusion')

@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    return response


CORS(breakfast, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(lunch, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(dinner, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(smoothies, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(desserts, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(snacks, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(analytics_form, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(workout, origins=['http://localhost:3000'], supports_credentials=True)
# CORS(chat, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(breakfast, url_prefix='/api/v1/breakfast')
# app.register_blueprint(lunch, url_prefix='/api/v1/lunch')
# app.register_blueprint(dinner, url_prefix='/api/v1/dinner')
# app.register_blueprint(snacks, url_prefix='/api/v1/smoothies')
# app.register_blueprint(smoothies, url_prefix='/api/v1/snacks')
# app.register_blueprint(desserts, url_prefix='/api/v1/desserts')
# app.register_blueprint(analytics_form, url_prefix='/api/v1/form')
# app.register_blueprint(workout, url_prefix='/api/v1/workout')
# app.register_blueprint(chat, url_prefix='/api/v1/chat')



if __name__ == '__main__':
    print('tables connected')
    app.run(debug=DEBUG, port=PORT)








