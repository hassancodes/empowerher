# this file is just fo dealing with databases
import pymongo
import pprint
client = pymongo.MongoClient("mongodb+srv://mhassan:622883@questiondb.ow3iutv.mongodb.net/?retryWrites=true&w=majority")
# creating a database named empower
db = client.empower



def addquestions(data):
    # collections are a part of the database
    dblist = db.list_collection_names()
    if "questions" in dblist:
        pass
    else:
        db.create_collection("questions")

    col = db.questions
    col.insert_one(data)


def retrievequestions():
    retquestions = db.questions
    # returns a lists to display
    return list(retquestions.find())


