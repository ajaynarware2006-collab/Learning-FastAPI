from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def intro():
    welcome={
        "Message":"Welcome to the App"
    }
    return welcome

@app.get("/student/{student_id}")
def student_info(student_id : int):
    details={
        "roll_no":student_id,
        "Name":"Ajay",
        "Branch":"AIML",
        "Status":"Recived"
    }

    return details