from models import Book,Author,Member,Category,Publisher
import storage
from utils import *
from datetime import date
#=========== Menu Functions =============

#=-= Statistics Menu Functions =-=
#calculate total books (all)
def calculate_total_books(books: list[Book]) -> int:
    return len(books)

def show_total_books():
    pass 

def show_total_members():
    pass

def show_total_publishers():
    pass

def show_total_authors():
    pass

def show_currently_borrowed_books():
    pass

def show_available_books():
    pass

#=-= Author Management Menu Functions =-=
def add_author():
    pass

def update_author():
    pass

def delete_author():
    pass

def view_author():
    pass

def view_all_authors():
    pass

#=-= Publisher Management menu Functions =-=
def add_publisher():
    pass

def update_publisher():
    pass

def delete_publisher():
    pass

def view_publisher():
    pass


def view_all_publishers():
    pass

#=-= Search Menu Functions =-=
def search_by_book_id():
    pass


def search_by_title():
    pass


def search_by_author():
    pass


def search_by_category():
    pass


def search_by_publisher():
    pass


def search_by_publication_year():
    pass


def advanced_search():
    pass

#=-= Borrowing Feature Menu Functions =-=
#to borrow book, from one member, to one book (checkif both available)
def borrow_book(member_id: str, book_id: str) -> bool:
    return
# to return book
def return_book(member_id: str, book_id: str) -> bool:
    return

#=-= Member Management Menu Functions =-=
#get the books borrowed by a member
def get_member_borrowed_books(member_id:str) -> list[Book]:
    return

def add_member():
    pass

def update_member():
    pass

def delete_member():
    pass

def view_member():
    pass

def view_all_members():
    pass


#=-= Book Management Menu Functions =-=
#Function to add a book object
def add_book() -> None:
    return

#update existing book
def update_book(
    book_id: str,
    title: str | None = None,
    author: Author | None = None,
    publisher: Publisher | None = None,
    category: str | None = None,
    published_date : date | None = None
) -> bool:
    return

#to delete a book, returns True if exists and deleted, else False
def delete_book(book_id: str) -> bool:
    return


#to get all books in list
def get_all_books() -> list[Book]:
    return

#get book by criteria
def get_books_by(
    book_id: str | None = None,
    year: int | None = None,
    month: int | None = None,
    author_name: str | None = None,
    category: str | None = None,
    publisher_id: str | None = None,
) -> list[Book]:
    return storage.get_books_by_criteria_from_database(
        book_id=book_id,
        year=year,
        month=month,
        author_name=author_name,
        category=category,
        publisher_id=publisher_id,
    )

#get Book object after finding it, None if not found
def get_book(book_id: str) -> Book | None:
    return


