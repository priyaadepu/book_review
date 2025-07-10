def test_create_review(client):
    """Test creating a review for a book"""
    # First create a book
    book_data = {
        "title": "Book to Review",
        "author": "Review Author"
    }
    book_response = client.post("/books/", json=book_data)
    book_id = book_response.json()["id"]
    
    # Create a review
    review_data = {
        "reviewer_name": "John Doe",
        "rating": 5,
        "comment": "Excellent book!"
    }
    
    response = client.post(f"/books/{book_id}/reviews", json=review_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["reviewer_name"] == "John Doe"
    assert data["rating"] == 5
    assert data["comment"] == "Excellent book!"
    assert data["book_id"] == book_id

def test_get_book_reviews(client):
    """Test getting reviews for a book"""
    # Create a book
    book_data = {"title": "Reviewed Book", "author": "Popular Author"}
    book_response = client.post("/books/", json=book_data)
    book_id = book_response.json()["id"]
    
    # Create a review
    review_data = {
        "reviewer_name": "Alice", 
        "rating": 5, 
        "comment": "Great!"
    }
    client.post(f"/books/{book_id}/reviews", json=review_data)
    
    # Get all reviews
    response = client.get(f"/books/{book_id}/reviews")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["reviewer_name"] == "Alice"