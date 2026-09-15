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

# ============== Category enum class =================
class Category(Enum):
    HORROR = "Horror"
    SCIENCE_FICTION = "Sci-Fi"
    FICTION = "Fiction"
    THRILLER = "Thriller"

#=========== Book class ==========
@dataclass
class Book:
    book_id : str
    title : str
    author : Author
    publisher : Publisher
    category : Category
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



