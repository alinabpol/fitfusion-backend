from peewee import *

DATABASE = SqliteDatabase('nutrition.sqlite')


class Nutrition(Model):
    title = CharField()
    description = CharField()
    time = TimeField()

    class Meta:
        database = DATABASE

class Analytics(Model):
    activity = CharField()
    time = TimeField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Nutrition, Analytics], safe=True)
    print("TABLES Created")
    DATABASE.close()