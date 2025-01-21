from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name:str # Required
    description: str|None=None # Optional
    price: float # Required
    category: str # Required
    discount: float=20.5 # default 'float' value of 20

@app.get("/")
def root():
    return "Welcome to E-Commerce Website"

@app.post("/post_product/")
def post_product(product:Product):
    product_dict= product.model_dump() # Create a dict object of the product class
    price_after_discount = round(((100-product.discount)/100)*product.price,2)
    product_dict.update({"price_after_discount":price_after_discount}) # Update with new key
    """ # code below if you want to add price_after_discount at front
    product_dict = {"price_after_discount":price_after_discount}
    product_dict.update(product.model_dump())
    """
    return product_dict

# This below code for adding an index and also taking product in request
@app.put("/product/{product_id}")
def update_product(product_id:int, product:Product, available:bool|None=None): # user can provide product_id as well as what Product class want
    # stuff ={"product_id":product_id}
    # stuff.update(product.model_dump())
    stuff = {"product_id":product_id, **product.model_dump()}
    if available:
        stuff.update({"is_available":True})
    return stuff
