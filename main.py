from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import books, reviews
from database import Base, engine
from app.models.books import Book
from app.models.reviews import Review

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Review Service",
    description="A service for managing books and reviews with caching support",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(books.router)
app.include_router(reviews.router)

@app.get("/")
async def root():
    return {
        "message": "Book Review Service API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "book-review-api"}
