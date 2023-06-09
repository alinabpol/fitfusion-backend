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
custom_collection = db['custom']


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
        result = lunch_collection.insert_one(document)
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
        result = dinner_collection.insert_one(document)
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
        result = snacks_collection.insert_one(document)
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
        result = smoothies_collection.insert_one(document)
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
        result = desserts_collection.insert_one(document)
        return result.inserted_id
    

class Custom:
    
    TITLE_MAX_LENGTH = 100
    INGREDIENTS_MAX_LENGTH = 500
    DESCRIPTION_MAX_LENGTH = 1000


    def __init__(self, title, time, ingredients, description, file):
        self.title = str(title)[:self.TITLE_MAX_LENGTH]
        self.time = int(time)
        self.ingredients = str(ingredients)[:self.INGREDIENTS_MAX_LENGTH]
        self.description = str(description)[:self.DESCRIPTION_MAX_LENGTH]
        self.file = str(file)

    # save data to database
    def save(self):
        document = {
            'title': self.title,
            'time': self.time,
            'ingredients': self.ingredients,
            'description': self.description,
            'file': self.file
        }
        result = custom_collection.insert_one(document)
        return result.inserted_id
    






