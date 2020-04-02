from  pymongo import MongoClient
import praw
from datetime import datetime

#Connexion à la BDD
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client["sentiments"]
collection = db["crawl"]

#Récupération des topics reddit
reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

#Catégorie de récupération
subreddit = reddit.subreddit('news')
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
            jsonStr = {"title": post.title, "contenu": post.selftext, "reaction": comment.body, "date": format(dateCom), "score": comment.score, "social_network": 'REDDIT'}
            #On insère la donnée dans la BDD
            collection.insert_one(jsonStr)