from fastapi import FastAPI
from pydantic import BaseModel , Field

app=FastAPI()

class Student(BaseModel):
    name:str=Field(min_length=2 ,max_length=50)
    email:str=Field(min_length=10 ,max_length=50)
    password:str=Field(min_length=8,max_length=50)
    brach:str=Field(min_length=2 ,max_length=10)

class StudentResponse(BaseModel):
    name:str=Field(min_length=2 ,max_length=50)
    email:str=Field(min_length=10 ,max_length=50)
    brach:str=Field(min_length=2 ,max_length=10)



@app.post("/student", response_model=StudentResponse)
def register(student:Student):
    return student.model_dump()