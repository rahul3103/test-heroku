import os
from flask import Flask, render_template
from subprocess import call
from peewee import CharField, PostgresqlDatabase, create_model_tables
from urllib.parse import urlparse
from flask_peewee.db import Database


if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    url = urlparse(DATABASE_URL)
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port
    }
else:
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': 'heroku'
    }


app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)


class Users(db.Model):
    name = CharField()
    email = CharField()


@app.route('/')
def welcome():
    call('printenv')
    a = 'Default'
    b = 'Default'
    if os.environ.get('DATABASE_URL'):
        a = os.environ.get('DATABASE_URL')
    if os.environ.get('HEROKU'):
        b = os.environ.get('HEROKU')
    create_model_tables([Users], fail_silently=True)
    Users.insert(name='John', email='Doe').execute()
    return render_template('index.html', a=a, b=b)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
