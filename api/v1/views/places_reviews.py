#!/usr/bin/python3
'''Contains the places_reviews view for the API.'''
from flask import abort, jsonify, make_response, request
from models import storage
from api.v1.views import app_views
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET'], strict_slashes=False)
def all_place_reviews(place_id):
    """Retrieves a Places reviews"""
    obj = storage.get(Place, place_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict() for obj in objs.values())


@app_views.route('/reviews/<review_id>',
                 methods=['GET'], strict_slashes=False)
def one_review(review_id):
    """retrieve one review"""
    review = storage.get("Review", review_id)
    if review:
        return jsonify(review.to_dict()), 200
    else:
        abort(404)


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_place_review(place_id, review_id):
    """delete a review on place id and return status code 200"""
    place = storage.get(place, place_id)
    if place:
        review = storage.get("Review", review_id)
        if review and review in place.review:
            storage.delete(amenity)
            storage.save()
            storage.close()
            return make_response(jsonify({}), 200)
        else:
            abort(404)
    else:
        abort(404)


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def post_review(review_id):
    """Returns the new review on place with the status code 201"""
    new_obj = request.get_json()
    if not new_obj:
        abort(400, "Not a JSON")
    if 'user_id' not in new_obj:
        return "Missing user_id", 400
    if not storage.get('User', dic.get('user_id')):
        abort(404)
    if 'name' not in new_obj:
        abort(400, "Missing name")
    if not storage.get('Place', place_id):
        abort(404)
    obj = Review(**new_obj)
    setattr(review, 'place_id', place_id)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/reviews/<review_id>',
                 methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """Updates a review of place object """
    obj = storage.get("Review", review_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for k, v in req.items():
        if k not in ['id', 'created_at', 'updated_at']:
            setattr(obj, k, v)

    storage.save()
    return make_response(jsonify(obj.to_dict()), 200)
