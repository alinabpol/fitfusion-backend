from peewee import *

DATABASE = SqliteDatabase('nutrition.sqlite')


class Nutrition(Model):
    title = CharField()
    description = CharField()
    time = TimeField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Nutrition], safe=True)
    print("TABLES Created")
    DATABASE.close()