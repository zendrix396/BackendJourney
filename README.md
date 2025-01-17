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

- 4 Types of HTTP Methods (Operation): POST (create), GET (read), PUT (update), DELETE (delete) => CRUD [Exotic ones: OPTIONS,HEAD,PATCH,TRACE]
- OpenAPI schema powers the interactive api dashboards of doc and redoc
```localhost:8000/openapi.json```
- We can create methods in 2 ways either with def root() or async def root()
### We use async/await when doing io operation (db), fetching api requests or other function responses etc (faster than normal function) => go through AsyncAwaitUsage.py for proper understanding
- function here are called **path operation function** and decorator is known as **path operation decorator**
=======

