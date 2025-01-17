# BACKEND Programming using FAST API

### DAY 1 [16-01-2025]

#### Setting up virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
pip install fastapi[all] uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt]
pip freeze > requirements.txt
```

#### Next step: Creating first fast api app

### created a main.py file and populated it with below content
```python
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

```

- importing fastapi then having a books dictionary
- defining a root function using @app.get("/")
- defining a "/books/{book_id}" endpoint which can contain data like "/books/1?include_author=1"
- include_author: Union[bool,None] means if not initialized default value is None

### Starting the fastapi server using the command
```bash
echo "you should be inside the virtual environment"
fastapi dev main.py

```
