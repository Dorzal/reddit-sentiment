from pymongo import MongoClient

def retrieveData():
    client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
    db = client["sentiments"]
    collection = db["polarite"]



    return 'hello boy'