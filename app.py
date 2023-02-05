from flask import Flask,request,redirect
from flask import render_template
from db import addquestions, retrievequestions
import pymongo
app = Flask(__name__)


# database
client = pymongo.MongoClient("mongodb+srv://mhassan:<password>@questiondb.ow3iutv.mongodb.net/?retryWrites=true&w=majority")
db = client.Questiondb
print(db)

name = "Hello"
@app.route("/")
def home():
    name = "hassan"
    return render_template("index.html", name=name)



@app.route("/assistance")

def assistance():
    # asking for the questions 

    return render_template("assistance.html")



@app.route("/askquestion", methods=["GET", "POST"])
# adding data to the database
def askquestion():
    title = request.form["title"]
    description = request.form["description"]
    data = {
            "title" : title,
            "description": description
            }
    
    addquestions(data)
    # this where we need to add a successfully asked question page
    return "You submitted"

@app.route("/freqask")
def freqask():
    data = retrievequestions()
    print(dict(data))

    # for i in data:
    #     print(i["title"])
    #     print(i["description"])
    #     print("/n")
    print(data)
    return data

    



app.run(debug=True)

