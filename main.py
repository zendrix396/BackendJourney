from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return "Welcome to E-Commerce Website"

@app.get("/category/{category}/feedback/{feedback}/")
def root(category: str, buy:bool,feedback:str,price:int=1000):
    return {"Category":category,"Price":price, "BuyOrNot":buy,"Feedback":feedback}



# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item