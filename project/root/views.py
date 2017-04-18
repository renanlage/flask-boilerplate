from flask import jsonify
from flask.blueprints import Blueprint

root_bp = Blueprint('root', __name__)


@root_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello world!'})


@root_bp.route('/health', methods=['GET'])
def health():
    return '', 200


@root_bp.route('/error', methods=['GET'])
def error():
    raise Exception('This is a view that raises an error')
