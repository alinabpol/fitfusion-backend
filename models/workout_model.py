from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("ATLAS_URI"))
db = client['fitfusion']
collection = db['workout']

# main blueprint class for nutrition models
class Workout:
    def __init__(self, activity, time, calories, link):
        self.activity = str(activity)
        self.time = int(time)
        self.calories = int(calories)
        self.link = link


    # save data to database
    def save(self):
        document = {
            'activity': self.activity,
            'time': self.time,
            'calories': self.calories,
            'link': self.link
        }
        result = collection.insert_one(document)
        return result.inserted_id
    



