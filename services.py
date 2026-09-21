from models import Book,Author,Member,Category,Publisher,MemberStatus
import storage
from utils import *
from datetime import date
#=========== Menu Functions =============

#=-= Statistics Menu Functions =-=
#calculate total books (all)
def calculate_total_books(books: list[Book]) -> int:
    print("~~~~ Function ~~~~")
    return len(books)

def show_total_books():
    print("~~~~ Function ~~~~")
    pass 

def show_total_members():
    print("~~~~ Function ~~~~")
    pass

def show_total_publishers():
    print("~~~~ Function ~~~~")
    pass

def show_total_authors():
    print("~~~~ Function ~~~~")
    pass

def show_currently_borrowed_books():
    print("~~~~ Function ~~~~")
    pass

def show_available_books():
    print("~~~~ Function ~~~~")
    pass

#=-= Publisher Management menu Functions =-=
def get_publisher(connection) :
    publisher_id = get_id("publisher")
    
    publisher = storage.get_publisher_from_database(
        connection,
        publisher_id
    )

    return publisher if publisher is not None else None
        
    
def add_publisher(connection):
    print("~~~~ Add Publisher Function ~~~~")
    while True:
        publisher_id = get_id("publisher")
        if storage.publisher_exists(connection, publisher_id):
            print("Publisher Exists")
            continue
        break
    publisher_name = get_name("publisher")
    city = get_city()

    new_publisher = Publisher(
        publisher_id,
        publisher_name,
        city
    )

    storage.insert_publisher_to_database(
        connection,
        new_publisher
    )

    print("New Publisher has been added\n")
    print(f"{'Publisher ID':<20} : {new_publisher.publisher_id}")
    print(f"{'Publisher Name':<20} : {new_publisher.publisher_name}")
    print(f"{'Publisher City':<20} : {new_publisher.publisher_city}\n")



def update_publisher(connection):
    print("~~~~ Update Publisher Function ~~~~")
    publisher = get_publisher(connection)

    if publisher is None:
        print("Publisher not Found")
        return

    new_publisher_name = get_name("publisher")
    new_city = get_city()

    updated = storage.update_publisher_in_database(
        connection,
        publisher.publisher_id,
        new_publisher_name,
        new_city
    )

    if updated:
        print("Update Successful\n")
        print(f"-------------- {publisher.publisher_name.upper()} -------------")
        print(f"{'Publisher ID':<20} : {publisher.publisher_id}")
        print(f"{'Publisher Name':<20} : {publisher.publisher_name}")
        print(f"{'Publisher City':<20} : {publisher.publisher_city}\n")
        return

    print("Update Failed\n")


def delete_publisher(connection):
    print("~~~~ Delete Publisher Function ~~~~")
    publisher = get_publisher(connection)

    if publisher is None:
        print("Publisher not Found")
        return
    
    deleted = storage.delete_publisher_from_database(
        connection,
        publisher.publisher_id
    )

    if deleted:
        print("Deletion Successful\n")
        return

    print("Deletion Failed\n")


def view_publisher(connection):
    print("~~~~ View a Publisher Function ~~~~")
    publisher = get_publisher(connection)

    if publisher is None:
        print("Publisher not Found")
        return

    print(f"-------------- {publisher.publisher_name.upper()} -------------")
    print(f"{'Publisher ID':<20} : {publisher.publisher_id}")
    print(f"{'Publisher Name':<20} : {publisher.publisher_name}")
    print(f"{'Publisher City':<20} : {publisher.publisher_city}\n")


def view_all_publishers(connection):
    print("~~~~ View all Publishers Function ~~~~")
    publisher_list = storage.fetch_all_publishers_from_database(connection)

    if not publisher_list:
        print("No Publisher in database.\n")
        return

    for publisher in publisher_list:
        print(f"===== {publisher.publisher_name} =====")
        print(f"{'Publisher ID':<20} : {publisher.publisher_id}")
        print(f"{'Publisher Name':<20} : {publisher.publisher_name}")
        print(f"{'Publisher City':<20} : {publisher.publisher_city}\n")

    return


#=-= Author Management Menu Functions =-=
def get_author(connection):
    author_id = get_id("author")
    author = storage.get_author_from_database(connection, author_id)

    return author if author is not None else None

def add_author(connection):
    print("~~~~ Add Author Function ~~~~")
    while True:
        author_id = get_id("author")
        if storage.author_exists(connection, author_id):
            print("Author Exists")
            continue
        break

    author_name = get_name("author")

    new_author = Author(author_id,author_name)
    storage.insert_author_to_database(
        connection,
        new_author
    )
    print("New Author has been added\n")

def update_author(connection):
    print("~~~~ Update Author Function ~~~~")
    author = get_author(connection)
    if author is None:
        print("Author not Found")
        return

    new_author_name = get_name("author")
    updated = storage.update_author_in_database(
        connection,
        author.author_id,
        new_author_name
    )

    if updated:
        print("Update Succesfull\n")
        return

    print("Update Failed\n")

def delete_author(connection):
    print("~~~~ Delete Author Function ~~~~")
    author = get_author(connection)

    if author is None:
        print("Author not Found")
        return

    deleted = storage.delete_author_from_database(connection, author.author_id)
    if deleted :
        print("Deletion Successfull\n")
        return

    print("Deletion Failed\n")
          
def view_author(connection):
    print("~~~~ View an Author Function ~~~~")
    author = get_author(connection)
    if author is None:
        print("Author not Found")
        return

    print(f"{'Author ID':<10} : {author.author_id}")
    print(f"{'Name':<10} : {author.author_name}\n")

def view_all_authors(connection):
    print("~~~~View all Author Function ~~~~")
    author_list = storage.fetch_all_authors_from_database(connection)

    if not author_list:
        print("No Author in Database\n")
        return
    
    for author in author_list:
        print("--------------------------------------------")
        print(f"{'Author ID':<10} : {author.author_id}")
        print(f"{'Name':<10} : {author.author_name}\n")

    return

#=-= Member Management Menu Functions =-=
#get the books borrowed by a member
def get_member_borrowed_books(member_id:str) -> list[Book]:
    print("~~~~ Function ~~~~")
    return

def get_member(connection):
    member_id = get_id("member")

    member = storage.get_member_from_database(
        connection,
        member_id
    )
    return member if member is not None else None

def add_member(connection):
    print("~~~~ Add Member Function ~~~~")

    while True:
        member_id = get_id("member")
        if storage.member_exists(connection, member_id):
            print("Member Exists")
            continue
        break

    member_name = get_name("member")
    member_email = get_email()
    member_status = MemberStatus.ACTIVE

    new_member = Member(
        member_id,
        member_name,
        member_email,
        member_status
    )

    storage.insert_member_to_database(
        connection,
        new_member
    )

    print("New Member has been added\n")


def update_member(connection):
    print("~~~~ Update Member Function ~~~~")
    member = get_member(connection)   

    if member is None:
        print("Member not Found")
        return

    new_member_name = get_name("member")
    new_email = get_email()

    updated = storage.update_member_in_database(
        connection,
        member.member_id,
        new_member_name,
        new_email,
        member.member_status.value
    )

    if updated:
        print("Update Successful\n")
        return

    print("Update Failed\n")


def delete_member(connection):
    print("~~~~ Delete Member Function ~~~~")
    member = get_member(connection)

    if member is None:
        print("Member not Found")
        return

    deleted = storage.delete_member_from_database(
        connection,
        member.member_id
    )

    if deleted:
        print("Deletion Successful\n")
        return

    print("Deletion Failed\n")

def deactivate_member(connection):
    print("~~~~ Deactivate Member Function ~~~~")
    member = get_member(connection)

    if member is None:
        print("Member not Found")
        return

    if member.member_status == MemberStatus.INACTIVE:
        print("Member is already inactive")
        return

    member.member_status = MemberStatus.INACTIVE
    updated = storage.update_member_in_database(
        connection,
        member.member_id,
        member.member_name,
        member.member_email,
        member.member_status.value
    )

    if updated:
        print("Update Successful\n")
        return

    print("Update Failed\n")

def activate_member(connection):
    print("~~~~ Activate Member Function ~~~~")
    member = get_member(connection)

    if member is None:
        print("Member not Found")
        return

    if member.member_status == MemberStatus.ACTIVE:
        print("Member is already active")
        return

    member.member_status = MemberStatus.ACTIVE
    updated = storage.update_member_in_database(
        connection,
        member.member_id,
        member.member_name,
        member.member_email,
        member.member_status.value
    )

    if updated:
        print("Update Successful\n")
        return

    print("Update Failed\n")


def view_member(connection):
    print("~~~~ View a Member Function ~~~~")
    member = get_member(connection)
    if member is None:
        print("Member not Found")
        return

    print(f"{'Member ID':<15} : {member.member_id}")
    print(f"{'Member Name':<15} : {member.member_name}\n")
    print(f"{'Member Email':<15} : {member.member_email}\n")
    
def view_all_members(connection):
    print("~~~~ View all Members Function ~~~~")
    member_list = storage.fetch_all_members_from_database(connection)

    if not member_list:
        print("No Member in Database")
        return

    for member in member_list:
        print("--------------------------------------------")
        print(f"{'Member ID':<15} : {member.member_id}")
        print(f"{'Member Name':<15} : {member.member_name}")
        print(f"{'Member Email':<15} : {member.member_email}")
        print(f"{'Member Status':<15} : {member.member_status.value}\n")
    return

#=-= Search Menu Functions =-=
def search_by_book_id():
    print("~~~~ Function ~~~~")
    pass


def search_by_title():
    print("~~~~ Function ~~~~")
    pass


def search_by_author():
    print("~~~~ Function ~~~~")
    pass


def search_by_category():
    print("~~~~ Function ~~~~")
    pass


def search_by_publisher():
    print("~~~~ Function ~~~~")
    pass


def search_by_publication_year():
    print("~~~~ Function ~~~~")
    pass


def advanced_search():
    print("~~~~ Function ~~~~")
    pass

#=-= Borrowing Feature Menu Functions =-=
#to borrow book, from one member, to one book (checkif both available)
def borrow_book(member_id: str, book_id: str) -> bool:
    print("~~~~ Function ~~~~")
    return
# to return book
def return_book(member_id: str, book_id: str) -> bool:
    print("~~~~ Function ~~~~")
    return
    
#=-= Book Management Menu Functions =-=
#Function to add a book object
def add_book(connection) -> None:
    print("~~~~ Add a Book Function ~~~~")
    book_id = get_id("book")
    title = get_title()
    authors = get_authors_sequence(connection)
    publisher = get_publisher(connection)
    categories = get_categories_sequence(connection)
    available = True
    published_date = get_published_date()

    new_book = Book(
        book_id=book_id,
        title=title,
        authors=authors,
        publisher=publisher,
        categories=categories,
        available=available,
        published_date=published_date
    )

    storage.insert_book_into_database(connection,new_book)
    storage.insert_book_and_corresponding_authors_into_database(connection,new_book.book_id, authors)
    storage.insert_book_and_corresponding_categories_into_database(connection,new_book.book_id, categories)




#update existing book
def update_book(
    book_id: str,
    title: str | None = None,
    publisher: Publisher | None = None,
    published_date : date | None = None
) -> bool:
    print("~~~~ Function ~~~~")
    return

#to delete a book, returns True if exists and deleted, else False
def delete_book(book_id: str) -> bool:
    print("~~~~ Function ~~~~")
    return


def view_all_books():
    print("~~~~ Function ~~~~")
    pass


def view_book():
    print("~~~~ Function ~~~~")
    pass


#to get all books in list
def get_all_books() -> list[Book]:
    print("~~~~ Function ~~~~")
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
    print("~~~~ Function ~~~~")
    return storage.get_books_by_criteria_from_database(
        book_id=book_id,
        year=year,
        month=month,
        author_name=author_name,
        category=category,
        publisher_id=publisher_id,
    )

#get category sequence
def get_categories_sequence(connection):
    category_list = []
    while True:
        category_id = get_category_id()
        if category_id is None :
            return category_list
        
        if storage.category_exists(connection,category_id):
            category = storage.get_category_from_database(connection, category_id)
            if category not in category_list:
                category_list.append(category)

        while True:
            more = input("Add more category? (Y/N)").strip().lower()
            if more == "n" :
                return category_list
            elif more == "y" :
                break
            print("INVALID")

def get_authors_sequence(connection):
    authors_list = []
    while True:
        author_id = get_id("author")
        author = storage.get_author_from_database(connection,author_id)

        if author is None :
            print("Author not Found")
        elif author not in authors_list:
            authors_list.append(author)        

        while True:
            more = input("Add more author? (Y/N)").strip().lower()
            if more == "n" :
                return authors_list
            elif more == "y" :
                break
            print("INVALID")
        


#get Book object after finding it, None if not found
def get_book(book_id: str) -> Book | None:
    print("~~~~ Function ~~~~")
    return