from peewee import *

database = MySQLDatabase('ershouche', **{'host': 'localhost', 'password': 'root', 'port': 3306, 'user': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Dmoz(BaseModel):
    description = TextField(null=True)
    link = TextField(null=True)
    title = TextField(null=True)

    class Meta:
        db_table = 'dmoz'