from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


client = MongoClient(os.getenv("ATLAS_URI"))
db = client['fitfusion']

breakfast_collection = db['breakfast']
lunch_collection = db['lunch']
dinner_collection = db['dinner']
snacks_collection = db['snacks']
smoothies_collection = db['smoothies']
desserts_collection = db['desserts']


class Breakfast:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    



class Lunch:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    



class Dinner:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    



class Snacks:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    



class Smoothies:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    




class Desserts:
    def __init__(self, title, img, time, ingredients, description):
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'img': self.img,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description
        }
        result = breakfast_collection.insert_one(document)
        return result.inserted_id
    






