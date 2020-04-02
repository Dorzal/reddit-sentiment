from textblob import TextBlob
from pymongo import MongoClient
from pprint import pprint
from bson.son import SON
import json

client = MongoClient('mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test?authSource=admin&replicaSet=python-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sentiments']['crawl'].aggregate([
    {
        '$group': {
            '_id': {
                'day': {
                    '$dayOfYear': '$date'
                }, 
                'hour': {
                    '$hour': '$date'
                }, 
                'title': '$title'
            },
            'comments': {
                '$push': {
                    'date': '$date', 
                    'reaction': '$reaction', 
                    'title': '$title'
                }
            }
        }
    }, {
        '$group': {
            '_id': '$_id.title', 
            'comments': {
                '$push': '$$ROOT'
            }
        }
    }
])

pprint(list(result))

# res = {}
# for post in listPosts:
#     for comment in post:
#         blob = TextBlob(comment)
#         for sentence in blob.sentences:
#             print()

# blob = TextBlob("hello")

# blob.tags
# blob.noun_phrases

# for sentence in blob.sentences:
#     if (sentence.sentiment.polarity != 0):
#         print(sentence)
#         print(sentence.sentiment.polarity)
