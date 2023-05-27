from peewee import *

DATABASE = SqliteDatabase('nutrition.sqlite')
DATABASE = SqliteDatabase('analytics.sqlite')
DATABASE = SqliteDatabase('workout.sqlite')


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

class Workout(Model):
    activity = CharField()
    time = TimeField()
    calories = IntegerField()
    link = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Nutrition, Analytics, Workout], safe=True)
    print("TABLES Created")
    DATABASE.close()