import os
from flask import Flask, render_template
from subprocess import call
from peewee import create_model_tables
from model import Users


app = Flask(__name__)


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
