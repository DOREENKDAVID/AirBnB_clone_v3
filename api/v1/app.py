#!/usr/bin/python3
""" flask web application API"""

from  os import getenv
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
"""flask instance"""
"""Register the blueprint to your Flask app"""
app.register_blueprint(app_views)
"""Set up CORS with your Flask app"""
CORS(app)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def flask_teardown(exception):
    """ closes the storage"""
    storage.close()


@app.errorhandler(404)
def errorhandler_404(error):
    """handle Not found error code 404"""
    response = {'error': 'Not found'}
    return jsonify(response), 404


if __name__ == "__main__":
    """run the host and port using environment variables"""
    HOST =getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
