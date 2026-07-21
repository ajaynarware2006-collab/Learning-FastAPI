from fastapi import FastAPI

app=FastAPI()

@app.post("/contact")
def contact():
    return{
        "message":"Contact request received successfully"
    }


#Request body
@app.post("/product")
def product(product:dict):
    product={
        "name": "Mechanical Keyboard",
        "price": 2499,
        "brand": "Logitech"
    }
    return {
        "Information":product
    }