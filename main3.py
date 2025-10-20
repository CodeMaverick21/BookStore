from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]

app = FastAPI()

class Book (BaseModel):
    id : int
    title : str
    author : str
    year : int

@app.get("/books")
def get_books(author: str = None, year: int = None):
    results = books
    if author:
        results = [b for b in results if b["author"].lower() == author.lower()]
    if year:
        results = [b for b in results if b["year"] == year]
    return results

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for b in books:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
def create_book(book : Book):
    books.append(book)
    return  {"message": "Book added", "book" : book}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i,b in enumerate(books):
        if b["id"] == book_id:
            books[i] = updated_book
            return {"message" : "Book updated", "book" : updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i,b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
