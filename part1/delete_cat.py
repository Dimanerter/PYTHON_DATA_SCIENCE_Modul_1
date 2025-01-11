from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://erterujamp:RB7ydmry8ldG0rV9@erter.krt7i.mongodb.net/?retryWrites=true&w=majority&appName=ERTER",
    server_api=ServerApi("1"),
)

db = client.book
db.cats.delete_one({"name": "barsik"})
result = db.cats.find_one({"name": "barsik"})
print(result)
