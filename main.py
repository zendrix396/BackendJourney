from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to Book Store!"

# @app.get("/price/{price}")
# def cost(price):
#     return f"The Book's Price is ${price}"
@app.get("/price/{price}")
def cost(price:int):
    return f"The Book's Price is ${price}"
