from textblob import TextBlob
from pymongo import MongoClient
from pprint import pprint
import datetime
import time
import os
#Connexion à la BDD
client = MongoClient(os.environ["MONGO_CONNECTION_STRING"])
crawl = client['sentiments']['crawl']
polarite = client['sentiments']['polarite']

def parsePolarite():
    # requête aggregate qui récupère les commentaires reddit triés par post et par date/heure
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
                # création d'un objet textblob qui permet de faire des analyses sur du texte
                blob = TextBlob(text)
                blob.tags
                blob.noun_phrases

                # On analyse la polarité de chaque phrase de chaque commentaire
                for sentence in blob.sentences:
                    avgPolarite += sentence.sentiment.polarity
                    avgPolarite = avgPolarite / 2
                
                jsonStrDelete = {
                    'title': title,
                    'reaction': text,
                    'date': date
                }

                # Pour limiter la taille de la BDD on supprime les données qui ont déjà été analysées
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

            # Si l'analyse de polarité n'existe pas encore on l'insert sinon on modifie celle qui existe
            if not existing_polarite:
                polarite.insert_one(jsonStrInsert)
            else:
                polarite.update_one(existing_polarite, {'$set': jsonStrInsert})

# On boucle sur l'execution du script pour que le parsing se fasse en continu
while True:
    parsePolarite()
    time.sleep(60)