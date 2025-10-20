# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# app = FastAPI()

# books = [
#     {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
#     {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
#     {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#     {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
#     {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
# ]

# class Book(BaseModel):
#     title : str
#     author : str
#     year : int

# @app.get('/')
# def read_root():
#     return {"Hello" : "World"}
# # path parameter
# # get all books
# @app.get('/books')
# def get_all_books():
#     return books

# # get retrive single book
# @app.get('/books/{book_id}')
# def get_single_book(book_id : int):
#     # get a specific book by id
#     for book in books:
#         if book["id"] == book_id:
#             return book
#     return {"message" : "Book not found"}

# # query parameter
# # GET - Retrive books by filtering using query parameters
# @app.get("/books")
# def get_books(author : str | None, year : str | None):
#     filtered_book = books
#     if author:
#         return {'author' : author}
#     if year:
#         return {'year' : year}
#     return {"message" : "Not found"}



# @app.post("/books")
# def create_book(book : Book):
#     new_id = max(b["id"] for b in books) + 1 if books else 1 
#     new_book = {
#         "id" : new_id ,
#         "title" : book.title,
#         "author" : book.author,
#         "year" : book.year
#     }

#     book.append(new_book)

#     return {"message" : "Book created successfully" , "book" : new_book}

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

