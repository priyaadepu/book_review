from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book.

    - Validates input data using Pydantic schema
    - Invalidates cache after successful creation
    - Returns the created book with generated ID
    """
    try:
        return BookService.create_book(db, book_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating book: {str(e)}"
        )

@router.get("/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    """
    Get all books with caching support.
    
    - First attempts to retrieve from Redis cache
    - Falls back to database if cache is unavailable
    - Implements proper error handling for cache failures
    """
    try:
        return BookService.get_books(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching books: {str(e)}"
        )

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get a specific book by ID.
    """
    book = BookService.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book
