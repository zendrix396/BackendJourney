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