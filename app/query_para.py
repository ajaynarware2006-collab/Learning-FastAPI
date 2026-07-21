from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def main():
    intro={
        "Message":"Demostration of Query parameters"
    }
    return intro


@app.get("/books")
def get_books(genre : str = "Programming" , limit : int = 10 , available : bool = True):
    if available:
        info={
            "genre": genre,
            "limit": limit
        }

    else:
        return {"message" : "Book is not available"}

    return info