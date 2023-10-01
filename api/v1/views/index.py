#!/usr/bin/python3
'''Contains the index view for the API.'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON """
    response = {'status':'OK'}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stat():
    """returns the number of each objects by type"""
    status = (
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User')
    )
    return jsonify(status)
