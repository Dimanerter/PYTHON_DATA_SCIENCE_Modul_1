from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://erterujamp:RB7ydmry8ldG0rV9@erter.krt7i.mongodb.net/?retryWrites=true&w=majority&appName=ERTER",
    server_api=ServerApi("1"),
)


db = client.book

result = db.cats.find_one({"_id": ObjectId("677eea130c8a709ffcffb67b")})
print(result)

result = db.cats.find({})

for cat in result:
    print(cat)
