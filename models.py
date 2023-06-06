from peewee import *

DATABASE = SqliteDatabase('workout.sqlite')
DATABASE = SqliteDatabase('analytics.sqlite')
DATABASE = SqliteDatabase('lunch.sqlite')
DATABASE = SqliteDatabase('dinner.sqlite')
DATABASE = SqliteDatabase('snacks.sqlite')
DATABASE = SqliteDatabase('smoothies.sqlite')
DATABASE = SqliteDatabase('desserts.sqlite')
DATABASE = SqliteDatabase('breakfast.sqlite')



class Breakfast(Model):
    title = CharField()
    img = CharField()
    time = IntegerField()
    ingredients = IntegerField()
    description = CharField()

    class Meta:
        database = DATABASE

class Lunch(Model):
    title = CharField()
    img = CharField()
    time = IntegerField()
    ingredients = IntegerField()
    description = CharField()

    class Meta:
        database = DATABASE

class Dinner(Model):
    title = CharField()
    img = CharField()
    time = IntegerField()
    ingredients = IntegerField()
    description = CharField()

    class Meta:
        database = DATABASE

class Desserts(Model):
    title = CharField()
    img = CharField()
    time = IntegerField()
    ingredients = IntegerField()
    description = CharField()

    class Meta:
        database = DATABASE

class Snacks(Model):
    title = CharField()
    img = CharField()
    ingredients = IntegerField()
    description = CharField()

    class Meta:
        database = DATABASE

class Smoothies(Model):
    title = CharField()
    img = CharField()
    time = IntegerField()
    ingredients = IntegerField()
    description = CharField()

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
    DATABASE.create_tables([ Analytics, Workout, Breakfast, Lunch, Dinner, Snacks, Smoothies, Desserts], safe=True)
    print("TABLES Created")
    DATABASE.close()