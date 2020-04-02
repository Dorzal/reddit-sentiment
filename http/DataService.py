from pymongo import MongoClient
import re

def retrieveData(subject):
    client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
    db = client["sentiments"]
    collection = db["polarite"]

    rgx = re.compile('.*'subject'.*', re.IGNORECASE)

    myquery = { "sujet": rgx }

    mydoc = mycol.find(myquery)
    
    return mydoc