from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.review import ReviewResponse, ReviewCreate
from app.services.book_service import BookService
from app.services.review_service import ReviewService

router = APIRouter(prefix="/books", tags=["reviews"])

@router.get("/{book_id}/reviews", response_model=List[ReviewResponse])
async def get_book_reviews(book_id: int, db: Session = Depends(get_db)):
    book = BookService.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    reviews = ReviewService.get_reviews(db, book_id)
    return reviews

@router.post("/{book_id}/reviews", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(book_id: int, review_data: ReviewCreate, db: Session = Depends(get_db)):
    review = ReviewService.create_review(db, book_id, review_data)
    if not review:
        raise HTTPException(status_code=404, detail="Book not found")
    return review
