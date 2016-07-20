from flask import jsonify
from flask.blueprints import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index():
    return jsonify('hello_world')
