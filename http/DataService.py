from pymongo import MongoClient
import re
import request

#recupére les datas ou appel le crawler
def retrieveData(subject):

    #connexion à la base de données mongo
    client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
    db = client["sentiments"]
    collection = db["polarite"]

    #regex like 
    rgx = re.compile('.*'subject'.*', re.IGNORECASE)

    myquery = { "sujet": rgx }

    #recherche en fonction de la requete 
    mydoc = mycol.find(myquery)

    # si retour alors renvoi la collection sinon appel crawler
    if(mydoc):
        return mydoc
    else:
        callCrawler(subject)
        return 'loader'

#appel crawler via POST
def callCrawler(subject):
    url = "http://crawler_by_id:5000"
    data = {"search": subject}

    requests.post(url, data)