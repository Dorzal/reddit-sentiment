from  pymongo import MongoClient
from pprint import pprint
import praw
from datetime import date
import json
import bson 
from bson.codec_options import CodecOptions

#Connexion à la BDD
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client["sentiments"]
collection = db["crawl"]

#Récupération des topics reddit
reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

#Catégorie de récupération
subreddit = reddit.subreddit('python')
hot_topic = subreddit.hot(limit=2)

tabPost = []
#Récupération des infos
for post in hot_topic:    
    comments = post.comments.list()
    for comment in comments:
        if comment.score > 1:
            jsonStr = bson.BSON.encode({'title': post.title, 'contenu': post.selftext, 'reaction': comment.body, 'date': format(date.today()), 'score': post.score})
            collection.insert_one(jsonStr)