"""from  pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")

db = client["sentiments"]
collection = db["crawl"]

post = {"id": 0, "name": "nico", "score": 5}
collection.insert_one(post)"""

import praw

reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', user_agent='ProjetTendanceV1')

subreddit = reddit.subreddit('python')

hot_topic = subreddit.hot(limit=5)

for post in hot_topic:
    print()
    print('Titre: {}, Ups: {}, Downs : {}, Is video : {}'.format(post.title, post.ups, post.downs, post.selftext))
    print()
    
    comments = submission.comments.list()
    for comment in comments:
        print(30*'-')
        print('Parent ID : ', comment.parent())
        print('Comment ID : ', comment.id)
        print(comment.body)