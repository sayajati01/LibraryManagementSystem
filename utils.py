from models import Book,Author,Member,Category,Publisher
from datetime import date, datetime
import re

# =========================================================
# GET FUNCTIONS
# =========================================================

def get_id(object_name: str) -> str:
    """
    Generate an ID based on object type.

    Examples:
        get_id("author")    -> AUT20260001
        get_id("publisher") -> PUB20260001
        get_id("member")    -> MEM20260001
        get_id("book")      -> BOOK20260001
        get_id("borrowing") -> BOR20260001

    The sequence should eventually come from the database.
    """
    prefixes = {
        "author": "AUT",
        "publisher": "PUB",
        "member": "MEM",
        "book": "BOOK",
        "borrowing":"BOR",
    }

    prefix = prefixes.get(object_name.lower())

    if prefix is None:
        raise ValueError(f"Unknown object type: {object_name}")

    # Placeholder sequence.
    # Later, SQLite will determine the next number.
    sequence = "0001"

    return f"{prefix}{date.today().year}{sequence}"


def get_name(object_name: str) -> str:
    while True:
        name = input(f"{object_name.capitalize()} name: ").strip()
        if validate_name(name): 
            return name

        raise ValueError(f"Invalid {object_name} name.")  


def get_email() -> str:
    while True:
        email = input("Email: ").strip()

        if validate_email(email):
            return email

        print("INVALID EMAIL")


def get_title() -> str:
    while True:
        title = input("Book title: ").strip()

        if validate_title(title):
            return title

        print("INVALID TITLE")


def get_author() -> Author:
    # This will eventually interact with your service/storage
    # to find an existing Author.
    author_id = input("Author ID: ").strip()

    if not validate_id(author_id, "author"):
        raise ValueError("INVALID AUTHOR ID")

    # Placeholder until your database/service layer exists.
    raise NotImplementedError


def get_category() -> Category:
    while True:
        category_input = input("Category: ").strip()

        try:
            category_input = Category(category_input)
        except ValueError:
            print("INVALID CATEGORY")
            continue

        if validate_category(category_input):
            return category_input


def get_publisher() -> Publisher:
    publisher_id = input("Publisher ID: ").strip()

    if not validate_id(publisher_id, "publisher"):
        raise ValueError("INVALID PUBLISHER ID")

    # Eventually:
    # return services.get_publisher(publisher_id)

    raise NotImplementedError


def get_published_date() -> date:
    while True:
        date_input = input("Published date (YYYY-MM-DD): ").strip()

        if not validate_published_date(date_input):
            print("INVALID DATE")
            continue

        return datetime.strptime(date_input, "%Y-%m-%d").date()


# =========================================================
# VALIDATION FUNCTIONS
# =========================================================

def validate_id(object_name: str, object_id: str) -> bool:
    """
    Validate an ID according to its object type.

    Examples:
        validate_id("author", "AUT20260001")
        validate_id("book", "BOOK20260001")
    """

    prefixes = {
        "author": "AUT",
        "publisher": "PUB",
        "member": "MEM",
        "book": "BOOK",
        "borrowing": "BOR"
    }

    prefix = prefixes.get(object_name.lower())

    if prefix is None:
        return False

    pattern = rf"^{prefix}\d{{8}}$"

    return bool(re.fullmatch(pattern, object_id))


def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.fullmatch(pattern, email))


def validate_name(name: str) -> bool:
    return bool(name.strip()) and len(name.strip()) <= 100


def validate_title(title: str) -> bool:
    return bool(title.strip()) and len(title.strip()) <= 200


def validate_author(author: Author) -> bool:
    return (
        isinstance(author, Author)
        and validate_id("author", author.author_id)
        and validate_name(author.name)
    )


def validate_category(category: Category) -> bool:
    return isinstance(category, Category)


def validate_published_date(published_date: str) -> bool:
    try:
        datetime.strptime(published_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_publisher(publisher:Publisher) -> bool:
    return isinstance(publisher, Publisher)


# =========================================================
# VALIDATE A BOOK
# =========================================================

def validate_book(book: Book) -> bool:
    return (
        isinstance(book, Book)
        and validate_id("book", book.book_id)
        and validate_title(book.title)
        and validate_author(book.author)
        and validate_category(book.category)
        and validate_publisher(book.publisher)
        and isinstance(book.published_date, date)
    )
