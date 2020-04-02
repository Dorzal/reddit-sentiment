from  pymongo import MongoClient
import praw
from datetime import datetime
from praw.models import MoreComments
import time

#Connexion à la BDD
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client["sentiments"]
collection = db["crawl"]

def recupDonnees ():
    #Récupération des topics reddit
    reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

    #Catégorie de récupération
    subreddit = reddit.subreddit('news')
    hot_topic = subreddit.hot(limit=2)

    #Récupération des infos
    for post in hot_topic:
        #On récupère la liste des commentaires
        comments = post.comments.list()
        for comment in comments:
            if isinstance(comment, MoreComments):
                continue
            if (not(comment.author == None) and (comment.score > 50)):
                #On formate la date    
                dateCom = datetime.fromtimestamp(comment.created)
                jsonStr = {"title": post.title, "contenu": post.selftext, "reaction": comment.body, "date": dateCom, "score": comment.score, "social_network": 'REDDIT'}
                #On vérifie que le commentaire n'existe pas
                existing_document = collection.find_one(jsonStr)
                if not existing_document:
                    #On insère la donnée dans la BDD
                    collection.insert_one(jsonStr)

while True:
    recupDonnees()
    time.sleep(3600)