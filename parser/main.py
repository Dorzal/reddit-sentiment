from textblob import TextBlob
from pymongo import MongoClient
client = MongoClient("mongodb+srv://sentiment:iYZQsvRbKy9SdXnx@python-9sotq.mongodb.net/test")
db = client.sentiments

polarite = client.polarite

blob = TextBlob("hello")

# if blob.detect_language() != 'en':
#     blob_en = blob.translate(to='en')
# else:
#     blob_en = blob
blob_en = blob

blob_en.tags
blob_en.noun_phrases

for sentence in blob_en.sentences:
    if (sentence.sentiment.polarity != 0):
        print(sentence)
        print(sentence.sentiment.polarity)