
from flask import Flask, jsonify, g
from flask_cors import CORS

DEBUG = True
PORT = 8000

import models

from resources.nutrition import nutrition

from resources.analytics_form import analytics_form

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


CORS(nutrition, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(nutrition, url_prefix='/api/v1/nutrition')
app.register_blueprint(analytics_form, url_prefix='/api/v1/form')



if __name__ == '__main__':
    print('tables connected')
    models.initialize()
    app.run(debug=DEBUG, port=PORT)








