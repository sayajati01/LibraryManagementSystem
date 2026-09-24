from models import Book,Author,Member,Publisher,Category
from datetime import date, datetime
import re

# =========================================================
# GET FUNCTIONS
# =========================================================
def get_category_id() -> str :
    prefix = "CAT"
    while True:
        try:
            sequence = input("Category ID : ").strip()

            if sequence == "":
                return None

            end = f"{int(sequence):04d}"
            return prefix+end
        except ValueError:
            print("INVALID ID")

def get_id(object_name: str, required=True) -> str:
    """
    ID based on input

    Examples:
        get_id("author")    -> AUT20260001
        get_id("publisher") -> PUB20260001
        get_id("member")    -> MEM20260001
        get_id("book")      -> BOOK20260001
        get_id("borrowing") -> BOR20260001

    The sequence is from input
    """
    prefixes = {
        "author": "AUT",
        "publisher": "PUB",
        "member": "MEM",
        "book": "BOOK",
        "borrowing":"BOR"
    }

    prefix = prefixes.get(object_name.lower())

    if prefix is None:
        raise ValueError(f"Unknown object type: {object_name}")

    while True:
        sequence = input(
            f"{object_name.capitalize()} ID: "
        ).strip()
        if not required and sequence == "":
            return None
        elif required and sequence == "":
            print("ID is required\n")
            continue

        object_id = f"{prefix}{date.today().year}{sequence}"
        if validate_id(object_name, object_id):
            return object_id
        
        print("INVALID ID")
        
    


def get_name(object_name: str) -> str:
    while True:
        name = input(f"{object_name.capitalize()} name: ").strip()
        if validate_name(name): 
            return name

        print(f"Invalid {object_name} name.")  


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


def get_category_name() -> Category:
    while True:
        category_input = input("Category: ").strip()

        try:
            category_input = Category(category_input)
        except ValueError:
            print("INVALID CATEGORY")
            continue

        if validate_category(category_input):
            return category_input

def get_city() -> str:
    while True :
        city_input = input("City: ").strip().title()

        if validate_city(city_input):
            return city_input

        print("INVALID CITY")



def get_published_date() -> date:
    while True:
        date_input = input("Published date (YYYY-MM-DD): ").strip()

        if not validate_published_date(date_input):
            print("INVALID DATE")
            continue

        return datetime.strptime(date_input, "%Y-%m-%d").date()
    
def get_current_date() -> date:
    return datetime.now.date()


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
        and validate_name(author.author_name)
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

def validate_city(city:str) -> bool:
    return bool(city) and len(city) <= 100


# =========================================================
# VALIDATE A BOOK
# =========================================================

def validate_book(book: Book) -> bool:
    return (
        isinstance(book, Book)
        and validate_id("book", book.book_id)
        and validate_title(book.title)
        and isinstance(book.published_date, date)
    )
