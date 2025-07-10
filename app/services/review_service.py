from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from app.models.reviews import Review
from app.models.books import Book
from app.schemas.review import ReviewCreate, ReviewResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books/{book_id}/reviews", response_model=ReviewResponse)
def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_review = Review(
        rating=review.rating,
        comment=review.comment,
        book_id=book_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/books/{book_id}/reviews", response_model=List[ReviewResponse])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return db.query(Review).filter(Review.book_id == book_id).all()
