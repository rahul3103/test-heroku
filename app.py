import os
from flask import Flask, render_template
from subprocess import call
from model import db_proxy, User


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
    User.insert(name='John', email='Doe').execute()
    return render_template('index.html', a=a, b=b)


if __name__ == '__main__':
    db_proxy.connect()
    db_proxy.create_tables([User], safe=True)
    app.run(port=5000, debug=True)
