from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    email:str
    age:int

@app.post("/register")
def register(user:User):
    return {
        "User":user.model_dump()
    }