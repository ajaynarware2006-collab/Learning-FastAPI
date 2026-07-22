from fastapi import FastAPI
from pydantic import BaseModel , Field

app=FastAPI()

class Movie(BaseModel):
    title:str = Field(min_length=3,max_length=50)
    rating:float = Field(ge=0 , le=10 )
    duration:int = Field(gt=0)

class MovieResponse(BaseModel):
    rating:float = Field(ge=0 , le=10 )
    duration:int = Field(gt=0)


@app.post("/movie",response_model=MovieResponse)
def movie(user:Movie):
    return {
        "message":"Movie Added Successfully",
        "movie":user.model_dump()
    }
