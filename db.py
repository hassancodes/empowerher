# this file is just fo dealing with databases
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

import pprint


client = pymongo.MongoClient(f"mongodb+srv://{os.getenv('USER')}:{os.getenv('PASSWORD')}@questiondb.ow3iutv.mongodb.net/?retryWrites=true&w=majority")
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


# adding stories to the app
def addstory(data):

    dblist = db.list_collection_names()
    if "secrets" in dblist:
        pass
    else:
        db.create_collection("secrets")

    secret = db.secrets 
    secret.insert_one(data)
    # {
    #  name :    
    #  title : " " 
    #  story : " "
    #  }

def fetchstories():
   secret = db.secrets
   return list(secret.find())

# print(fetchstories())


def  addunanweredquestions(data):
    dblist = db.list_collection_names()
    if "unansweredquestions" in dblist:
        pass
    else:
        db.create_collection("unansweredquestions")

    unansquestion = db.unansweredquestions
    unansquestion.insert_one(data)



