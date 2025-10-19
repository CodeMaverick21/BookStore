from fastapi import FastAPI
from pydantic import BaseModel
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]
app = FastAPI()

class Book(BaseModel):
    title : str
    author : str
    year : int
    
# path / query / request
@app.get("/")
def read_root():
    return { "Hello" : "World"}

@app.post("/books")
def create_book(book : Book):
    new_book = {
        "id" : 6,
        "title" : book.title,
        "author" : book.author,
        "year" : book.year
    }

    books.append(new_book)

    return{"message" : "Book created successfully", "Book" : new_book}
