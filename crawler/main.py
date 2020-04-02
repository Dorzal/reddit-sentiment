from  pymongo import MongoClient
from pprint import pprint
import praw
from datetime import date

class lePost:
    sujet=''
    contenu=''
    reaction=''
    date=''
    score=0

    def __init__(s,c,r,d,sco):
        self.sujet = s
        self.contenu = c
        self.reaction = r
        self.date = d
        self.score = sco

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
            """print(30*'-')
            print('Parent ID : ', comment.parent())
            print('Comment ID : ', comment.id)
            print(comment.body)"""
            monObjet = lePost(post.title, post.selftext, comment.body, date.today(), post.score)
            tabPost.append()

for p in tabPost:
    #print(p)
    collection.insert_one(p)