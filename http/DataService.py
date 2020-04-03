# coding= utf-8

from pymongo import MongoClient
import re
import requests
import json


def retrieveData(subject):


    client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
    db = client["sentiments"]
    collection = db["polarite"]

    rgx = re.compile('.*'+subject+'.*', re.IGNORECASE)

    myquery = { "sujet": rgx }

    mydoc = collection.find(myquery)

    if(mydoc):
        for x in mydoc:
            return x
    else:
        callCrawler(subject)
        return 'loader'

def callCrawler(subject):
    url = "http://crawler_by_id:5000"
    data = {"search": subject}

    requests.post(url, data)