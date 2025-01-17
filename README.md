# BACKEND Programming using FAST API

## Target: Implementing REST APIs, CRUD, caching, basic containerization and testing.

### Weeks 1-2: FastAPI Fundamentals
#### Core Concepts
- [X] ~~Python virtual environments & dependency management~~
- [X] ~~FastAPI project structure~~
- [X] ~~Pydantic models & data validation~~
- [X] ~~Async/await in FastAPI~~
- [ ] Request/Response handling
- [ ] Error handling & middleware basics
---
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

### Pydantic Usage for Basic Crud like Posting, Updating and Deleting Information
- importing Optional from typing, BaseModel from pydantic class
- creating a class for Book and BookUpdate that inherites from BaseModel
- Dictionary Unwrapping Concept {*a,*b} for BookUpdate method
- @app.get("/") for reading, @app.put("/path") for update, @app.delete("/path") for deletion and @app.post("/path) for posting new information

### Important Code Snippets
```python
# HTTPException Usage
if book_id not in books:
    raise HTTPException(status_code=404, detail="Book not found")

# exclude_unset=True => just contain keys that are being updated
update_data = book.dict(exclude_unset=True)

```

### Got to know: For Testing api CRUD methods of updating/deleting/putting you can either use curl or localhost:8000/docs/ for the gui interface of testing stuff by swagger
---
### DAY 2 [17-01-2025]

- 4 Types of HTTP Methods (Operation): POST (create), GET (read), PUT (update), DELETE (delete) => CRUD [Exotic ones: OPTIONS,HEAD,PATCH,TRACE]
- OpenAPI schema powers the interactive api dashboards of doc and redoc
```localhost:8000/openapi.json```
- We can create methods in 2 ways either with def root() or async def root()
### We use async/await when doing io operation (db), fetching api requests or other function responses etc (faster than normal function) => go through AsyncAwaitUsage.py for proper understanding
- function here are called **path operation function** and decorator is known as **path operation decorator**