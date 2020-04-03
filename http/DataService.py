# coding= utf-8

from pymongo import MongoClient
import re
import requests
import json
from flask import jsonify


def retrieveData(subject):


    client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
    db = client["sentiments"]
    collection = db["polarite"]

    rgx = re.compile('.*'+subject+'.*', re.IGNORECASE)

    myquery = { "title": rgx }

    mydoc = collection.find(myquery).sort("date")
    output = []
    if(mydoc):
        for x in mydoc:
            output.append({'title' : x['title'], 'date' : x['date'], 'polarite' : x['polarite'], 'social_network' : x['social_network']})
        return jsonify({'result' : output})
    else:
        callCrawler(subject)
        return jsonify({'result' : false})

def callCrawler(subject):
    url = "http://crawler_by_id:5000"
    data = {"search": subject}

    requests.post(url, data)