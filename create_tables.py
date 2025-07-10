from app.models.books import Book
from database import Base, engine

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
