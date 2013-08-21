import pymongo
from pymongo import Connection
connection = Connection()
db = connection['test']
collection = db.names
items = collection.find_one()
print items['name']
import datetime
post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
print post
posts = db.posts
posts.insert(post)
print posts
print posts.find_one()
new_posts = [{"author": "Mike",
                     "text": "Another post!",
                     "tags": ["bulk", "insert"],
                     "date": datetime.datetime(2009, 11, 12, 11, 14)},
                   {"author": "Eliot",
                     "title": "MongoDB is fun",
                     "text": "and pretty easy too!",
                     "date": datetime.datetime(2009, 11, 10, 10, 45)}]
posts.insert(new_posts)
for post in posts.find():
	print post
	
for post in posts.find({"author": "Mike"}):
	print post
	
