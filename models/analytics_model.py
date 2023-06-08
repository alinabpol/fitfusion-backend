from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("ATLAS_URI"))
db = client['fitfusion']
collection = db['analytics']

# main blueprint class for nutrition models
class Analytics:
    def __init__(self, activity, time):
        self.activity = str(activity)
        self.time = int(time)

    # save data to database
    def save(self):
        document = {
            'activity': self.activity,
            'time': self.time,
        }
        result = collection.insert_one(document)
        return result.inserted_id
    





