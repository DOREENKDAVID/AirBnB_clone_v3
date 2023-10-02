#!/usr/bin/python3
"""Contains the states view for the API."""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities', strict_slashes=False)
    """Retrieves the list of all places objects"""
    objs = storage.all(Place)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def single_place(place_id):
    """Retrieves a Places object"""
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())
