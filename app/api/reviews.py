from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.review import ReviewResponse, ReviewCreate
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["reviews"])

@router.get("/{book_id}/reviews", response_model=List[ReviewResponse])
async def get_book_reviews(book_id: int, db: Session = Depends(get_db)):
    """
    Get all reviews for a specific book.
    
    - Uses indexed query for optimal performance
    - Returns empty list if no reviews found
    - Validates book existence implicitly through FK constraint
    """
    try:
        # First check if book exists
        book = BookService.get_book_by_id(db, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
        
        reviews = BookService.get_book_reviews(db, book_id)
        return reviews
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching reviews: {str(e)}"
        )

@router.post("/{book_id}/reviews", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(book_id: int, review_data: ReviewCreate, db: Session = Depends(get_db)):
    """
    Create a new review for a book.
    
    - Validates book existence before creating review
    - Enforces rating constraints (1-5 stars)
    - Returns the created review with generated ID
    """
    try:
        review = BookService.create_review(db, book_id, review_data)
        if not review:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )
        return review
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating review: {str(e)}"
        )