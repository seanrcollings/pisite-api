from flask import Blueprint, jsonify, render_template
from app.models import Stat
from app import db
api = Blueprint('api', __name__)

@api.route('/')
def root():
    return "Pi Site API"
    
@api.route('/docs')
def docs():
    return render_template('docs.html')

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