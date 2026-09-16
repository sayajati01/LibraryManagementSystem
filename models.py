from dataclasses import dataclass
from enum import Enum
from datetime import date, datetime

# ============ Publisher class =============
@dataclass
class Publisher:
    publisher_id : str
    publisher_name : str
    publisher_city : str


# ============== Author class ================
@dataclass
class Author:
    author_id : str
    author_name : str
    

# ========= Member class ==========
@dataclass
class Member:
    member_id : str
    member_name : str
    member_email : str

# ============== Category class. ==================
@dataclass
class Category:
    category_id : str
    category_name : str

# ============== Categories enum class =================
class Categories(Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    MYSTERY = "Mystery"
    THRILLER = "Thriller"
    HORROR = "Horror"
    ROMANCE = "Romance"
    FANTASY = "Fantasy"
    SCIENCE_FICTION = "Science Fiction"
    HISTORICAL = "Historical"
    BIOGRAPHY = "Biography"
    AUTOBIOGRAPHY = "Autobiography"
    SELF_HELP = "Self-Help"
    PHILOSOPHY = "Philosophy"
    PSYCHOLOGY = "Psychology"
    SCIENCE = "Science"
    TECHNOLOGY = "Technology"
    BUSINESS = "Business"
    HISTORY = "History"
    POETRY = "Poetry"
    DRAMA = "Drama"
    CHILDREN = "Children"
    EDUCATION = "Education"
    TRAVEL = "Travel"
    COOKING = "Cooking"
    RELIGION = "Religion"
    OTHER = "Other"

#=========== Book class ==========
@dataclass
class Book:
    book_id : str
    title : str
    author : list[Author]
    publisher : Publisher | None
    category : list[Category]
    available : bool
    published_date : date


    def is_available(self) -> bool :
        return self.available

# ======== BORROWING class =======
@dataclass
class Borrowing:
    borrowing_id:str
    member_id:str
    book_id:str
    borrow_date:date
    return_date:date | None



