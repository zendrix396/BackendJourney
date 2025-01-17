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
### DAY 2 [17-01-2025]

Path Parameters Go through
- if same address in path operation decorator two times the first one is evaluated
- if two address /users/me and /users/{user_id} two separate users/me should be above /users/{users_id} or user_id="me"
- using enum to get predefined path parameters. (Example in code). Tne enum class you make contains the pre-defined parameters that can be provided in request, this class inherits from string and enum in our example
- for storing a path parameter containing a path if you try to do normally (/files/{file_path})it would give not found error, instead try doing (/files/{file_path:path}) so extra ":path" now file_path can contain a file path
```python
# creating an enum class
class PriceRange(str, Enum):
    BUDGET = "budget"
    MEDIUM = "medium"
    PREMIUM = "premium"

# getting a path parameter of path
@app.get("/path/{file_path:path}")
def path(file_path:str):
    return {"file_path":file_path}

```

### We'll discuss query parameters later, end of Day 2!

---