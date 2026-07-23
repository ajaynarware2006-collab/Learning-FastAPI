from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI()

class Contact(BaseModel):
    name:str=Field(max_length=50,min_length=2)
    email:str=Field(max_length=50,min_length=5)
    message:str=Field(max_length=256,min_length=0)

@app.get("/")
def welcome():
    return{
        "message":"Welcome to the portfolio",
        "api_versoin":4.1,
        "introduction":"I am Ajay Narware an AI Engineer Anthusiast building APIs using FastAPI"
    }

@app.get("/about")
def about():
    return{
        "name":"Ajay Narware",
        "role":"Student",
        "college":"IPSA",
        "branch":"CSA-AIML",
        "goal":"AI Engineer"
    }

@app.get("/skills")
def skills():
    return{
        "programimg":["python","SQL","Git"],
        "frameorks":["FastAPI","Pandas","Streamlit"],
        "database":["FastAPI"],
        "tools":[],

    }

@app.get("/education")
def education():
    return{
        "college":"IPSA",
        "degree":"Btech",
        "semester":"5th",
        "branch":"CSA-AIML"
    }

@app.get("/projects")
def projects():
    return{
        "project1":"about it",
        "project2":"about it",
        "project3":"about it",
        "project4":"about it",
    }


@app.post("/contact")
def post_contact(contact:Contact):
    return contact.model_dump()

@app.get("/socials")
def socials():
    return{
        "GitHub":"link",
        "LinkedIn":"link",
        "LeetCode":"link",
        "Email":"link",
        "Portfolio":"link"
    }

@app.get("/stats")
def stats():
    return{
        "project":10,
        "github Commits":164,
        "leetcode Problems":15,
        "tech stack":10
    }