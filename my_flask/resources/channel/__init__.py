from flask import Blueprint

from flask_restful import Api

from . import my_channel

user_bp = Blueprint('user_bp', __name__,)

user_api = Api(user_bp)
