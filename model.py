import os
from peewee import Model, CharField, PostgresqlDatabase
from urllib.parse import urlparse


if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    url = urlparse(DATABASE_URL)
    name = url.path[1:]
    user = url.username,
    password = url.password,
    host = url.hostname,
    port = url.port
    database = PostgresqlDatabase(name, user=user, password=password, host=host, port=port)
else:
    database = PostgresqlDatabase('heroku')


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    name = CharField()
    email = CharField()
