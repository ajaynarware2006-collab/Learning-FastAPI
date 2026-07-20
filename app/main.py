from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    details={
        "name": "Ajay Narware",
        "role": "Student",
        "goal": "AI engineer",
        "banch":"AIML"
    }
    return details