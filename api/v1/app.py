#!/usr/bin/python3
""" flask web application API"""

import os
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
def flask_teardown():
    """ closes the storage"""
    storage.close()


@app.errorhandler(404)
def errorhandler_404(error):
    """handle Not found error code 404"""
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    """run the host and port using environment variables"""
    app.run(host=getenv('HBNB_API_HOST') or '0.0.0.0',
            port=getenv('HBNB_API_PORT') or 5000,
            threaded=True)
