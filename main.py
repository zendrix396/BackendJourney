from typing import Optional # Required for Updation
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # Basically Used to create Objects for Stability

"""Pydantic models for data validation
Basically if you are 'posting' some information using curl or swagger,
you will do title="something" and author="something" so it will 
automatically create a dict of it using Book.dict()"""

app = FastAPI()

class Book(BaseModel): # Book Object
    title: str
    author: str

# here optional means your wish which property you want to update (optional)
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None

# Our "database" of books
books = {
    1: {"title": "Harry Potter", "author": "J.K. Rowling"},
    2: {"title": "Lord of the Rings", "author": "Tolkien"}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to our Book API!"}

@app.get("/books")
def list_books():
    return books

@app.get("/books/{book_id}")
def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@app.post("/books/{book_id}")
def create_book(book_id: int, book: Book): # Passing the Book Pydantic Class
    if book_id in books:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books[book_id] = book.dict() #convert pydantic model to dictionary
    return books[book_id]

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookUpdate):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    current_book = books[book_id]
    update_data = book.dict(exclude_unset=True)  # Only get the fields that were actually set
    books[book_id] = {**current_book, **update_data} # Dictionary Unpacking the latest data overrides the previous one
    return books[book_id]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    
    deleted_book = books.pop(book_id)
    return {"message": f"Book '{deleted_book['title']}' deleted successfully"}
