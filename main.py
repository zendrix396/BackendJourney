from fastapi import FastAPI, Query # Imported Query for query validation
from pydantic import BaseModel

from typing import Annotated 


app = FastAPI()

class Product(BaseModel):
    name:str # Required
    description: str|None=None
    price: float 
    category: str

@app.get("/")
def root():
    return "Welcome to E-Commerce Website"


# @app.put("/product/{product_id}")
# def update_product(product_id:int, product:Product, bought:int|None=Query(default=50,ge=0,le=500),available:bool|None=None): # user can provide product_id as well as what Product class want
#     stuff = {"product_id":product_id, **product.model_dump()}
#     if available:
#         stuff.update({"is_available":True})
#     stuff.update({"units_bought":bought})
#     return stuff


@app.put("/product/{product_id}")
def update_product(
    product_id: int,
    product: Product,
    bought: Annotated[int, Query(ge=20,le=500)]=50, # (optional value set to 50 by default)
    # bought: Annotated[int, Query(ge=20,le=500)]=..., # required value without any default val
    destination: Annotated[str, Query(
        pattern="^[A-Z][a-zA-Z]*(-[A-Z][a-zA-Z]*)+$", # Regex
        description="Hyphen-separated city names with capital letters"
    )]="Ghaziabad-Delhi",
    available: bool | None = None):

    stuff = {"product_id": product_id, **product.model_dump()}
    if available:
        stuff.update({"is_available": True})
    stuff.update({"units_bought": bought,"destination": destination.split("-")})
    
    return stuff