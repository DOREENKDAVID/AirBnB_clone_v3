#!/usr/bin/python3
"""
Contains the blueprint for the API
"""
from flask import Blueprint

""" Create a Blueprint instance with the URL prefix /api/v1"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

<<<<<<< HEAD
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
=======
>>>>>>> c640dbb957420f8585e040c1ce45fa03ffe2a8e1
