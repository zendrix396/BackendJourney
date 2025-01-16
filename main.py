from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Our "database" of books
books = {
    1: {"title": "Harry Potter", "author": "J.K. Rowling"},
    2: {"title": "Lord of the Rings", "author": "Tolkien"}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to our Book API!"}

@app.get("/books/{book_id}")
def read_book(book_id: int, include_author: Union[bool, None] = None):
    book = books.get(book_id)
    if not book:
        return {"error": "Book not found"}
    
    if include_author:
        return book
    return {"title": book["title"]}