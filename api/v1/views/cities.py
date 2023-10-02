#!/usr/bin/python3
'''Contains the cities view for the API.'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<states_id>/cities', methods=['GET'], strict_slashes=False)
def all_cities(state_id):
    """Retrieves the list of all city of a state objects"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    #convert objs to dictionaries and then to json
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def single_city(city_id):
    """Retrieves a City object"""
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """Deletes a City object"""
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)
    else:
        storage.delete(obj)
        storage.save()
        return make_response(jsonify({}), 200)


@app_views.route('/states/<states_id>/cities', methods=['POST'], strict_slashes=False)
def post_state(state_id):
    """Returns the new city of a state with the status code 201"""
    new_obj = request.get_json()
    if not new_obj:
        abort(400, "Not a JSON")
    if 'name' not in new_obj:
        abort(400, "Missing name")
    obj = State(**new_obj)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Updates a City object """
    obj = storage.get(City, city_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for key, val in req.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, val)

    storage.save()
    return make_response(jsonify(obj.to_dict()), 200)


@app.errorhandler(404)
def errorhandler_404(error):
    """handle Not found error code 404"""
    response = {'error': 'Not found'}
    return jsonify(response), 404


@app.errorhandler(400)
def errorhandler_400(error):
    """handle Bad Request error code 400"""
    response = {'error': 'Bad Request'}
    return jsonify(response), 400
