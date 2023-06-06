from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()

client= os.getenv("ATLAS_URI")
db = client['fitfusion']
collection = db['breakfast']

class Breakfast:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = collection.insert_one(document)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        result = collection.find()
        return list(result)

    @staticmethod
    def get_one(id):
        result = collection.find_one({'_id': ObjectId(id)})
        print(result)
        return result

    @staticmethod
    def update(id, data):
        result = collection.update_one({'_id': id}, {'$set': data})
        return result.modified_count

    @staticmethod
    def delete(id):
        result = collection.delete_one({'_id': id})
        return result.deleted_count






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