import os

from flask import Flask, g
from flask_cors import CORS
from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()


DEBUG = True
PORT = 8000



app = Flask(__name__)
connection_url = os.getenv("ATLAS_URI")
client = MongoClient(connection_url)
db = client['fitfusion']



from controllers.breakfast import breakfast
from controllers.lunch import lunch
from controllers.dinner import dinner
from controllers.snacks import snacks
from controllers.smoothies import smoothies
from controllers.desserts import desserts
from controllers.analytics import analytics
from controllers.workout import workout
from controllers.chat import chat
from controllers.custom import custom

app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db_mongo = client.get_database('fitfusion')

@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    db.client.close()
    return response


CORS(breakfast, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(lunch, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(dinner, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(smoothies, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(desserts, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(snacks, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(analytics, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(workout, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(chat, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)
CORS(custom, origins=['http://localhost:3000', 'http://192.168.0.12:3000'], supports_credentials=True)

app.register_blueprint(breakfast, url_prefix='/api/v1/breakfast')
app.register_blueprint(lunch, url_prefix='/api/v1/lunch')
app.register_blueprint(dinner, url_prefix='/api/v1/dinner')
app.register_blueprint(snacks, url_prefix='/api/v1/smoothies')
app.register_blueprint(smoothies, url_prefix='/api/v1/snacks')
app.register_blueprint(desserts, url_prefix='/api/v1/desserts')
app.register_blueprint(analytics, url_prefix='/api/v1/form')
app.register_blueprint(workout, url_prefix='/api/v1/workout')
app.register_blueprint(chat, url_prefix='/api/v1/chat')
app.register_blueprint(custom, url_prefix='/api/v1/custom')



if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)








