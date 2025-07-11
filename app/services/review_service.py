from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.reviews import Review
from app.models.books import Book
from app.schemas.review import ReviewCreate
import logging

logger = logging.getLogger(__name__)

class ReviewService:
    @staticmethod
    def create_review(db: Session, book_id: int, review_data: ReviewCreate) -> Optional[Review]:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None

        review = Review(**review_data.model_dump(), book_id=book_id)
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def get_reviews(db: Session, book_id: int) -> List[Review]:
        return db.query(Review).filter(Review.book_id == book_id).all()
