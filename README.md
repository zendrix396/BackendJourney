# BACKEND Programming using FAST API

## Target: Implementing REST APIs, CRUD, caching, basic containerization and testing.

### Weeks 1-2: FastAPI Fundamentals
#### Core Concepts
- [ ] Python virtual environments & dependency management
- [ ] FastAPI project structure
- [ ] Pydantic models & data validation
- [ ] Async/await in FastAPI
- [ ] Request/Response handling
- [ ] Error handling & middleware basics
---
### DAY 1

#### Setting up virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
pip install fastapi[all] uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt]
pip freeze > requirements.txt
```

#### Next step: starting up with fast api configuration using documentation
