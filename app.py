from flask import Flask,request,redirect
import os
from flask import render_template
from db import addquestions, retrievequestions,addstory,fetchstories,addunanweredquestions

app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")



@app.route("/assistance",methods=["GET"])

def assistance():
    # asking for the questions 

    return render_template("assistance.html")




#################################################
#################################################
@app.route("/askquestion", methods=["GET", "POST"])
# adding data to the database
def askquestion():
    title = request.form["title"]
    description = request.form["description"]
    data = {
            "title" : title,
            "description": description
            }
    addunanweredquestions(data)
    # addquestions(data)
    # this where we need to add a successfully asked question page
    return "You submitted"

@app.route("/submitpost",methods=["GET","POST"])
def submitpost():
    # call a function pull all the stories before that

    title = request.form["title"]
    story = request.form["story"]
    storydata = {
        "storytitle" : title,
        "storydescription": story
    }
    addstory(storydata)
    return "Story Submitted"






#################################################
#################################################


@app.route("/frequentask", methods=["GET"])
def frequentask():
    data = retrievequestions()
    return render_template("frequentask.html", data=data)
    # print(data)
    # return data

@app.route("/secretstories")    
def secretstories():
    # we will load the random stories
    storydata = fetchstories()
    # print(storydata[0]["storytitlep
    print(storydata)

    return render_template("secretstories.html", storydata=storydata)





if __name__== "__main__":
    app.run(debug=True)

