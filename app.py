from flask import Flask,request,redirect
from flask import render_template
from db import addquestions, retrievequestions
import pymongo
app = Flask(__name__)



@app.route("/")
def home():
    name = "hassan"
    return render_template("index.html")



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

@app.route("/frequentask")
def frequentask():
    data = retrievequestions()
    return render_template("frequentask.html", data=data)
    # print(data)
    # return data

@app.route("/secretstories")    
def secretstories():
    return render_template("secretstories.html")



app.run(debug=True)

