from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to the App"}


@app.get("/college")
def college_details():
    return {
        "College Name":"IPSA",
        "Branch":"AIML",
        "Semester":"5th"
    }


@app.get("/skills")
def get_skills():
    return ["python","FastAPI","PostgreSQL"]


@app.get("/goal")
def get_goal():
    return {
        "goal":"AI Engineer"
    }