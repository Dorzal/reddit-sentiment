from textblob import TextBlob
from pymongo import MongoClient
from pprint import pprint
from bson.son import SON
import datetime
import json

client = MongoClient('mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test')
crawl = client['sentiments']['crawl']
polarite = client['sentiments']['polarite']

listPosts = crawl.aggregate([
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

# pprint(list(listPosts))

res = {}
for post in listPosts:
    title = post['_id']
    res[title] = {}

    for commentHour in post['comments']:
        date = commentHour['comments'][0]['date']
        commentDate = date.replace(minute=0, second=0, microsecond=0)
        res[title][commentDate] = {}
        avgPolarite = 0

        for comment in commentHour['comments']:
            text = comment['reaction']
            blob = TextBlob(text)
            blob.tags
            blob.noun_phrases

            for sentence in blob.sentences:
                avgPolarite += sentence.sentiment.polarity
                avgPolarite = avgPolarite / 2
            
            jsonStrDelete = {
                'title': title,
                'reaction': text,
                'date': date
            }
            existing_crawl = crawl.find(jsonStrDelete)
            if existing_crawl:
                crawl.delete_many(jsonStrDelete)

        jsonStrInsert = {
            "title":  title,
            "date": commentDate,
            "social_network": 'REDDIT',
            "polarite": round(avgPolarite, 2)
        }
        existing_polarite = polarite.find_one(jsonStrInsert)

        if not existing_polarite:
            polarite.insert_one(jsonStrInsert)
        else:
            polarite.update_one(existing_polarite, {'$set': jsonStrInsert})