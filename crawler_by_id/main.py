from  pymongo import MongoClient
import praw
from datetime import datetime
from flask import Flask, json, request
from praw.models import MoreComments
from flask_cors import CORS

#Connexion à la BDD
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client["sentiments"]
collection = db["crawl"]

#Récupération des topics reddit
reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

def callSocialNetwork(recherche):

    #On passe le paramètre
    subreddit = reddit.subreddit(recherche)
    hot_topic = subreddit.hot(limit=10)

    #Récupération des infos
    for post in hot_topic:
        #On récupère la liste des commentaires
        comments = post.comments.list()
        for comment in comments:
            # On check que le prochain commentaire n'est pas un MoreComments
            if isinstance(comment, MoreComments):
                continue
            
                
            #On formate la date    
            dateCom = datetime.fromtimestamp(comment.created)
            jsonStr = {
                "title": post.title,
                "contenu": post.selftext,
                "reaction": comment.body,
                "date": dateCom,
                "score": comment.score,
                "social_network": 'REDDIT'
            }
            #On vérifie que le commentaire n'existe pas
            existing_document = collection.find_one(jsonStr)
            print("existing_document : ", existing_document)

            if not existing_document:
                print("jsonStr : ", jsonStr)    
                #On insère la donnée dans la BDD
                collection.insert_one(jsonStr)



#Creation de l'api
api = Flask(__name__)
CORS(api)

@api.route('/hello')
def hello_world():
    return 'Hello, World!'

@api.route('/', methods=['POST'])
def post_index():
    if request.form['search']:
        callSocialNetwork(request.form['search'])
    return 'ok'

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')