import os
from flask import Flask, render_template
from subprocess import call

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
    return render_template('index.html', a=a, b=b)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
