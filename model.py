import os
from peewee import Model, CharField, PostgresqlDatabase, Proxy
from urllib.parse import urlparse

db_proxy = Proxy()

if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    db = urlparse(DATABASE_URL)
    user = db.username
    password = db.password
    path = db.path[1:]
    host = db.hostname
    port = db.port
    database = PostgresqlDatabase(database=path, user=user, password=password, host=host, port=port)
    db_proxy.initialize(database)
else:
    database = PostgresqlDatabase('heroku')
    db_proxy.initialize(database)


class BaseModel(Model):
    class Meta:
        database = db_proxy


class User(BaseModel):
    name = CharField()
    email = CharField()
