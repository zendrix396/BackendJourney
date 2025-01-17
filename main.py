from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to Book Store!"

# @app.get("/price/high")
# def cost1():
#     return "The Book is costly"

# # @app.get("/price/{price}")
# # def cost(price): # will not give any error if price is not int
# #     return f"The Book's Price is ${price}"
@app.get("/price/{price}")
def cost(price:int): # will give error if price is not int
    return f"The Book's Price is ${price}"

from enum import Enum # enum is used if you want only specific types of request
#like for books category if someone is messing around giving weird categories you can create a category enum beforehand so that the request is only within that

# Create an Enum for book categories
class BookCategory(str, Enum): # Inherits from both str and Enum
    FICTION = "fiction"
    NON_FICTION = "non-fiction"
    SCIENCE = "science"
    HISTORY = "history"

# Create an Enum for price ranges
class PriceRange(str, Enum):
    BUDGET = "budget"
    MEDIUM = "medium"
    PREMIUM = "premium"


# Use the Enum in path parameter
@app.get("/category/{category}")
def get_books_by_category(category: BookCategory):
    if category == BookCategory.FICTION:
        return "Here are fiction books"
    elif category == BookCategory.NON_FICTION:
        return "Here are non-fiction books"
    elif category == BookCategory.SCIENCE:
        return "Here are science books"
    elif category == BookCategory.HISTORY:
        return "Here are history books"

@app.get("/price-range/{range}")
def get_books_by_price_range(range: PriceRange):
    price_ranges = {
        PriceRange.BUDGET: "Books under $10",
        PriceRange.MEDIUM: "Books between $10-$30",
        PriceRange.PREMIUM: "Books over $30"
    }
    return price_ranges[range]

@app.get("/path/{file_path:path}")
def path(file_path:str):
    return {"file_path":file_path}

