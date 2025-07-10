
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

@app.post("/test")
def test_book(book_data: BookCreate):
    return book_data
