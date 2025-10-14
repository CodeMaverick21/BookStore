from fastapi import FastAPI
app = FastAPI()

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]
@app.get('/')
def read_root():
    return {"Hello" : "World"}
# path parameter
# get all books
@app.get('/books')
def get_all_books():
    return books

# get retrive single book
@app.get('/books/{book_id}')
def get_single_book(book_id : int):
    # get a specific book by id
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message" : "Book not found"}

# query parameter
# GET - Retrive books by filtering using query parameters
@app.get("/books")
def get_books(author : str | None, year : str | None):
    filtered_book = books
    if author:
        return {'author' : author}
    if year:
        return {'year' : year}
    return {"message" : "Not found"}
