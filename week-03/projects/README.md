# Simple Data API

YThis is my week 3 project for lightweight **FastAPI** that demonstrates CRUD operations with validation, persistence, and testing.  

---

## Features
- **FastAPI** framework for building RESTful endpoints
- **Pydantic v2** models with strong validation
- **File-based persistence** using JSON storage
- **Full CRUD**: create, read, update, delete items
- **Pytest + httpx** integration tests
- **Linting & formatting** with Flake8 and Black

---

## Project Structure
simple_data_api/
│
├── app.py                # FastAPI app entrypoint
├── routes.py             # API routes (CRUD endpoints)
├── models.py             # Item model & dict conversion
├── validators.py         # Pydantic schemas (ItemCreate, ItemUpdate)
├── storage.py            # JSON-backed storage class
├── data.json             # Persistent data file
│
└── tests/                # Test suite
├── test_api.py           # API integration tests
├── test_models.py        # Model conversion tests
└── test_validators.py    #Validator rule tests


## Testing
cd simple_data_api
pip install -r requirements.txt


## Running the API
uvicorn app:app --reload

http://127.0.0.1:8000/docs #swagger

pytest -v

Data is persisted in data.json
