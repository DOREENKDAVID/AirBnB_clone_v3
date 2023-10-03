#!/usr/bin/python3
"""Contains the states view for the API."""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def all_place_amenities(place_id):
    """Retrieves a Places amenities"""
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict() for obj in objs.values())


@app_views.route('/places/<place_id>/Amenity/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_place_amenity(place_id, amenity_id):
    """dele amenity by place id and return status code 200"""
    place = storage.get(place, place_id)
    if place:
        amenity = storage.get("amenity", amenity_id)
        if amenity and amenity in place.amenities:
            storage.delete(amenity)
            storage.save()
            storage.close()
            return make_response(jsonify({}), 200)
        else:
            abort(404)
    else:
        abort(404)


@app_views.route('/places/<place_id>/Amenity/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def post_place_amenity(place_id, amenity_id):

    """update a new amenity by place id and return status code 200"""
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)
    if place and amenity:
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenity.append("amenity")
            storage.save()
            storage.close()
            return jsonify(amenity.to_dict()), 201
    else:
        abort(404)
