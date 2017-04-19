import os
from peewee import Model, CharField, PostgresqlDatabase
from urllib.parse import urlparse

if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    db = urlparse(DATABASE_URL)
    user = db.username
    password = db.password
    path = db.path[1:]
    host = db.hostname
    port = db.port
    database = PostgresqlDatabase(path, user=user, password=password, host=host, port=port)
else:
    database = PostgresqlDatabase('heroku')


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    name = CharField()
    email = CharField(null=False, unique=True)
