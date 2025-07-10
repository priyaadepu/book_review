from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.books import Book
from app.schemas.book import BookCreate
import logging

logger = logging.getLogger(__name__)

class BookService:
    @staticmethod
    def get_books(db: Session) -> List[Book]:
        return db.query(Book).all()

    @staticmethod
    def create_book(db: Session, book_data: BookCreate) -> Book:
        try:
            book = Book(**book_data.model_dump())
            db.add(book)
            db.commit()
            db.refresh(book)
            return book
        except Exception as e:
            db.rollback()
            logger.error(f"Failed to create book: {e}")
            raise

    @staticmethod
    def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
        return db.query(Book).filter(Book.id == book_id).first()
