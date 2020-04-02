#from pymongo import MongoClient
#from pprint import pprint

#client = MongoClient()

#db = client.admin
#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)
import praw

reddit = praw.Reddit(client_id ='fEQd43i9zHyhqA', client_secret='LpLwmKtOuUmrfdqhrlnYt8znvk4', username='W4rNoX', password='Cookies54', user_agent='ProjetTendanceV1')

subreddit = reddit.subreddit('popular')

hot_topic = subreddit.hot(limit=2)

for submission in hot_topic:
    if not submission.stickied:
        print()
        print('Titre: {}, Ups: {}, Downs : {}'.format(submission.title, submission.ups, submission.downs))
        print()
    
    """comments = submission.comments.list()
    for comment in comments:
        print(30*'-')
        print('Parent ID : ', comment.parent())
        print('Comment ID : ', comment.id)
        print(comment.body)"""