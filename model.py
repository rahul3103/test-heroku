import os
from peewee import Model, CharField
from playhouse.db_url import connect

database = connect(os.environ.get('DATABASE_URL') or 'sqlite:///default.db')


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    name = CharField()
    email = CharField()
