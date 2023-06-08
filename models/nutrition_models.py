from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()



client = MongoClient(os.getenv("ATLAS_URI"))
db = client['fitfusion']
collection = db['breakfast']

class BaseNutritionModel:
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
        result = collection.insert_one(document)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        result = collection.find()
        print(result)
        return list(result)

    @staticmethod
    def get_one(id):
        result = collection.find_one({'_id': ObjectId(id)})
        print(result)
        return result

    @staticmethod
    def update(id, data):
        result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        print(result.modified_count)
        return result.modified_count

    @staticmethod
    def delete(id):
        result = collection.delete_one({'_id': ObjectId(id)})
        print(result.deleted_count)
        return result.deleted_count




class Breakfast(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('breakfast')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)



class Lunch(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('lunch')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)



class Dinner(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('dinner')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)


class Snacks(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('snacks')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)


class Smoothies(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('smoothies')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)


class Desserts(BaseNutritionModel):
    def __init__(self, title, img, time, ingredients, description):
        super().__init__('desserts')
        self.title = str(title)
        self.img = str(img)
        self.time = int(time)
        self.ingredients = str(ingredients)
        self.description = str(description)


