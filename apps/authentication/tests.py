 
from django.test import TestCase

from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Fintechers']
user_collection = db['users']

# Query the users collection and print the result
users = user_collection.find()
for user in users:
    print(user)