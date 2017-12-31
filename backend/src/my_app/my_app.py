import os
# import mysql.connector
from flaskext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, abort, \
    jsonify, render_template
from logging import getLogger, StreamHandler, DEBUG
from pprint import pprint
import json
from json import JSONDecoder
from flask_cors import CORS

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py
CORS(app)

mysql = MySQL()
# Load default config and override config from an environment variable
app.config.update(dict(
    MYSQL_DATABASE_HOST='db',
    MYSQL_DATABASE_PORT=3306,
    MYSQL_DATABASE_USER='admin',
    MYSQL_DATABASE_PASSWORD='admin',
    MYSQL_DATABASE_DB='my_app',
    MYSQL_DATABASE_CHARSET='utf8',
    MYSQL_USE_UNICODE=True,
    # DATABASE=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(app.root_path))), 'myapp.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

mysql.init_app(app)


def connect_db():
    """Connects to the specific database."""
    return connector.cursor()


def init_db():
    mysql = MySQL()
    db = mysql.get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    return connect_db()


@app.route('/')
def show_entries():
    connector = mysql.connect()
    cur = connector.cursor()
    cur.execute('select * from heroes order by id desc')
    entries = cur.fetchall()
    columns = cur.description
    result = [{columns[index][0]: column for index, column in enumerate(value)} for value in entries]
    connector.close()
    return jsonify({'heroes': result})


@app.route('/<int:id>')
def show_hero(id):
    connector = mysql.connect()
    cur = connector.cursor()
    cur.execute('select * from heroes where id = {}'.format(id))
    hero = cur.fetchone()
    columns = cur.description
    result = {columns[index][0]: column for index, column in enumerate(hero)}
    connector.close()
    return jsonify({'hero': result})


@app.route('/', methods=['PUT'])
def update_hero():
    data = request.get_json()
    connector = mysql.connect()
    d = JSONDecoder()
    request_data = d.decode( json.dumps(data))
    cur = connector.cursor()
    cur.execute("update heroes set name = %(name)s where id = %(id)s;", request_data)
    connector.commit()
    connector.close()
    return jsonify({'result': 'ok'})


@app.route('/add', methods=['POST'])
def add_hero():
    data = request.get_json()
    connector = mysql.connect()
    d = JSONDecoder()
    request_data = d.decode( json.dumps(data))
    cur = connector.cursor()
    cur.execute("insert into heroes (id, name) values (null, %(name)s)", request_data)
    connector.commit()
    connector.close()
    return jsonify({'result': 'ok'})


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_hero(id):
    connector = mysql.connect()
    cur = connector.cursor()
    cur.execute("delete from heroes where id = %s", id)
    connector.commit()
    connector.close()
    return jsonify({'result': 'deleted'})


@app.route('/api/heroes')
def search_hero():
    name = request.args.get('name')
    connector = mysql.connect()
    cur = connector.cursor()
    cur.execute("select * from heroes where  name like %s", ("%" + name + "%"))
    heroes = cur.fetchall()
    columns = cur.description
    connector.close()
    # result = []
    # for hero in heroes:
    #     for index, column in enumerate(hero):
    #         result += {columns[index][0]: column}
    # pprint(result)
    # ここのデータの作り方を調べる
    result = [
        {'id': 2, 'name': 'hero2'},
        {'id': 3, 'name': 'hero3'},
        {'id': 4, 'name': 'hero4'},
    ]
    pprint(result)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
