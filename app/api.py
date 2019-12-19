from flask import Blueprint, jsonify
from app.models import Stat
from app import db
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def home():
    return '/stats - returns a list of all stats'

@api.route('/stats')
def stats():
    stats = Stat.query.all()
    return jsonify([i.serialize for i in stats])

@api.route('/stats/<int:_id>')
def show(_id):
    stat = Stat.query.get(_id)
    return jsonify(stat.serialize)

@api.route('/stats/<int:_id>/data')
def data(_id):
    stat_data = Stat.query.get(_id).execute_command()
    return stat_data