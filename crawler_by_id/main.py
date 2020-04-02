from  pymongo import MongoClient
import praw
from datetime import datetime
from flask import Flask, json, request

#Connexion à la BDD
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client["sentiments"]
collection = db["crawl"]

#Récupération des topics reddit
reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

#Creation de l'api
api = Flask(__name__)

@api.route('/', methods=['POST'])
def get_companies():
    data = request.form
    if data.search:
        callSocialNetwork(data.search)

if __name__ == '__main__':
    api.run()


def callSocialNetwork(recherche):

    #On passe le paramètre
    subreddit = reddit.subreddit(recherche)
    hot_topic = subreddit.hot(limit=1)

    #Récupération des infos
    for post in hot_topic:
        #On récupère la liste des commentaires
        comments = post.comments.list()
        for comment in comments:
            #if isinstance(comment, MoreComments):
            if comment.score > 10:
                #On formate la date    
                dateCom = datetime.fromtimestamp(comment.created)
                jsonStr = {
                    "title": post.title,
                    "contenu": post.selftext,
                    "reaction": comment.body,
                    "date": format(dateCom),
                    "score": comment.score,
                    "social_network": 'REDDIT'
                }
                #On vérifie que le commentaire n'existe pas
                existing_document = collection.find_one(jsonStr)
                if not existing_document:
                    #On insère la donnée dans la BDD
                    collection.insert_one(jsonStr)


