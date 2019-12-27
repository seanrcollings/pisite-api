from flask import Blueprint, jsonify, render_template
from app.models import Stat
from app import db
api = Blueprint('api', __name__)
from app.models import Stat
commands = [
    '/bin/date +"%I:%M %p"',
    '/bin/date +\\%d/\\%m/\\%Y',
    "/usr/bin/uptime | /bin/grep -o '...., ...., ....'",
    "/usr/bin/uptime | /bin/grep -o '..users'",
    "/bin/df -h --total | /bin/grep total | /bin/grep -o '..%'",
    "/bin/ps -Ao pid --sort=-pcpu | /usr/bin/head -n 2 | /usr/bin/tr -dc '0-9'",
    "/bin/ps -Ao pid --sort=-pcpu | /usr/bin/head -n 2 | /usr/bin/tr -dc '0-9'",
    "/bin/ps -o pmem --sort=-pmem | /usr/bin/head -n 2 | /usr/bin/tr -dc '0-9'",
    "/usr/bin/du -hs /var/www/pisite | /bin/grep -o '..M'",
]


@api.route('/')
def root():
    stats = Stat.query.all()
    for index, stat in enumerate(stats):
        stat.command = commands[index]
        db.session.add(stat)
    db.session.commit()
    return render_template('landing.html')


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