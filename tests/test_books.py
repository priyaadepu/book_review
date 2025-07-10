def test_create_book(client):
    """Test creating a new book"""
    book_data = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A classic American novel",
        "isbn": "978-0-7432-7356-5"
    }
    
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "The Great Gatsby"
    assert data["author"] == "F. Scott Fitzgerald"
    assert data["isbn"] == "978-0-7432-7356-5"
    assert "id" in data
    assert "created_at" in data

def test_get_books(client):
    """Test getting all books"""
    # Create a test book first
    book_data = {
        "title": "Test Book",
        "author": "Test Author"
    }
    client.post("/books/", json=book_data)
    
    response = client.get("/books/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Test Book"