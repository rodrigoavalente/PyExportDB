import os
from configuration import ROOT_PATH
from peewee import SqliteDatabase, Model, CharField

DBPATH = os.path.join(ROOT_PATH, "db.sqlite")
db = SqliteDatabase(DBPATH)


class BaseModel(Model):
    class Meta:
        database = db


class HostModel(BaseModel):
    username = CharField(max_length=63)
    password = CharField(max_length=63)
    host_url = CharField()

    def __str__(self):
        return "postgresql://{}:{}@{}:5432".format(self.username, self.password, self.host_url)

    class Meta:
        table_name = "hosts"


models = [HostModel]


def connect_to_local_db():
    db.connect()
    db.create_tables(models)

def disconnect_from_local_db():
    db.close()