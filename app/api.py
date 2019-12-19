from flask import Blueprint, jsonify
from app.models import Command
from app import db
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def home():
    return 'hello there'


@api.route('/stats')
def stats():
    stats = Command.query.all()
    return jsonify([i.serialize for i in stats])
