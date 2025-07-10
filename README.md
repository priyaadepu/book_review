# Book Review Service

A RESTful API service for managing books and reviews with Redis caching.

## Features

- CRUD operations for books and reviews
- Redis caching for improved performance
- Comprehensive error handling
- Automated testing
- OpenAPI/Swagger documentation

## API Endpoints

- `GET /books` - List all books
- `POST /books` - Create a new book
- `GET /books/{id}` - Get a specific book
- `GET /books/{id}/reviews` - Get reviews for a book
- `POST /books/{id}/reviews` - Create a review for a book

## Setup Instructions

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Start Redis server
6. Run the application: `uvicorn app.main:app --reload`
7. Visit http://localhost:8000/docs for API documentation

## Running Tests

```bash
pytest