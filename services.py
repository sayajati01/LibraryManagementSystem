from models import Book,Author,Member,Category,Publisher,MemberStatus,Borrowing
import storage
from utils import *
from datetime import date
#=========== Menu Functions =============

#=-= Statistics Menu Functions =-=
def display_statistics(connection) -> None:
    print("""
-------- LIBRARY STATISTICS --------
""")

    print(f"Total Books           : {storage.get_total_books(connection)}")
    print(f"Available Books       : {storage.get_available_books(connection)}")
    print(f"Borrowed Books        : {storage.get_borrowed_books(connection)}")
    print(f"Total Authors         : {storage.get_total_authors(connection)}")
    print(f"Total Publishers      : {storage.get_total_publishers(connection)}")
    print(f"Total Members         : {storage.get_total_members(connection)}")
    print(f"Active Members        : {storage.get_active_members(connection)}")
    print(f"Inactive Members      : {storage.get_inactive_members(connection)}")
    print(f"Total Borrowings      : {storage.get_total_borrowings(connection)}")
    print(f"Active Borrowings     : {storage.get_active_borrowings(connection)}")
    
#=-= Publisher Management menu Functions =-=
def get_publisher(connection,required) :
    view_all_publishers(connection)
    publisher_id = get_id("publisher",required)
    
    publisher = storage.get_publisher_from_database(
        connection,
        publisher_id
    )

    return publisher if publisher is not None else None
        
    
def add_publisher(connection):
    print("~~~~ Add Publisher Function ~~~~")
    while True:
        publisher_id = get_id("publisher",required=True)
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
    storage.display_publisher_with_given_id(connection,new_publisher.publisher_id)




def update_publisher(connection):
    print("~~~~ Update Publisher Function ~~~~")
    publisher = get_publisher(connection,required=True)

    if publisher is None:
        print("Publisher not Found")
        return

    storage.display_publisher_with_given_id(connection,publisher.publisher_id)

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
        storage.display_publisher_with_given_id(connection,publisher.publisher_id)
        return

    print("Update Failed\n")


def delete_publisher(connection):
    print("~~~~ Delete Publisher Function ~~~~")
    publisher = get_publisher(connection,required=False)

    if publisher is None:
        print("Publisher not Found")
        return
    storage.display_publisher_with_given_id(connection,publisher.publisher_id)
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
    publisher = get_publisher(connection,required=False)

    if publisher is None:
        print("Publisher not Found")
        return

    storage.display_publisher_with_given_id(connection,publisher.publisher_id)


def view_all_publishers(connection):
    print("~~~~ View all Publishers Function ~~~~")
    publisher_list = storage.fetch_all_publishers_from_database(connection)

    if not publisher_list:
        print("No Publisher in database.\n")
        return

    print(f"===== PUBLISHERS =====")
    for publisher in publisher_list:
        print(f"{publisher.publisher_id:<50}| {publisher.publisher_name:<20}| {publisher.publisher_city:<20}\n")

    return


#=-= Author Management Menu Functions =-=
def get_author(connection, required):
    author_id = get_id("author",required)
    author = storage.get_author_from_database(connection, author_id)

    return author if author is not None else None

def add_author(connection):
    print("~~~~ Add Author Function ~~~~")
    while True:
        author_id = get_id("author",required=True)
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
    storage.display_author_with_given_id(connection, new_author.author_id)

def update_author(connection):
    print("~~~~ Update Author Function ~~~~")
    author = get_author(connection,required=False)
    if author is None:
        print("Author not Found")
        return
    storage.display_author_with_given_id(connection, author.author_id)

    new_author_name = get_name("author")
    updated = storage.update_author_in_database(
        connection,
        author.author_id,
        new_author_name
    )

    if updated:
        print("Update Succesfull\n")
        storage.display_author_with_given_id(connection, author.author_id)
        return

    print("Update Failed\n")

def delete_author(connection):
    print("~~~~ Delete Author Function ~~~~")
    author = get_author(connection,required=False)

    if author is None:
        print("Author not Found")
        return
    storage.display_author_with_given_id(connection, author.author_id)

    deleted = storage.delete_author_from_database(connection, author.author_id)
    if deleted :
        print("Deletion Successfull\n")
        return

    print("Deletion Failed\n")
          
def view_author(connection):
    print("~~~~ View an Author Function ~~~~")
    author = get_author(connection,required=False)
    if author is None:
        print("Author not Found")
        return
    storage.display_author_with_given_id(connection, author.author_id)

def view_all_authors(connection):
    print("~~~~View all Author Function ~~~~")
    author_list = storage.fetch_all_authors_from_database(connection)

    if not author_list:
        print("No Author in Database\n")
        return
    
    print("--------------------------------------------")
    for author in author_list:
        print(f"{author.author_id:<15} : {author.author_name}")

    return

#=-= Member Management Menu Functions =-=
def get_member(connection,required:bool) -> Member | None:
    member_id = get_id("member",required)

    member = storage.get_member_from_database(
        connection,
        member_id
    )
    return member if member is not None else None

def add_member(connection):
    print("~~~~ Add Member Function ~~~~")

    while True:
        member_id = get_id("member",required=True)
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
    storage.display_member_with_given_id(connection,new_member.member_id)


def update_member(connection):
    print("~~~~ Update Member Function ~~~~")
    member = get_member(connection,required=False)   

    if member is None:
        print("Member not Found")
        return
    storage.display_member_with_given_id(connection,member.member_id)

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
        storage.display_member_with_given_id(connection,member.member_id)
        return

    print("Update Failed\n")


def delete_member(connection):
    print("~~~~ Delete Member Function ~~~~")
    member = get_member(connection,required=False)

    if member is None:
        print("Member not Found")
        return
    storage.display_member_with_given_id(connection,member.member_id)

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
    member = get_member(connection,required=False)

    if member is None:
        print("Member not Found")
        return
    
    storage.display_member_with_given_id(connection,member.member_id)

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
    member = get_member(connection,required=False)

    if member is None:
        print("Member not Found")
        return
    
    storage.display_member_with_given_id(connection,member.member_id)

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
        storage.display_member_with_given_id(connection,member.member_id)
        return

    print("Update Failed\n")


def view_member(connection):
    print("~~~~ View a Member Function ~~~~")
    member = get_member(connection,required=False)
    if member is None:
        print("Member not Found")
        return
    storage.display_member_with_given_id(connection,member.member_id)
    
def view_all_members(connection):
    print("~~~~ View all Members Function ~~~~")
    member_list = storage.fetch_all_members_from_database(connection)

    if not member_list:
        print("No Member in Database")
        return

    print("--------------------------------------------")
    for member in member_list:
        print(f"{member.member_id:<15}| {member.member_name:<15}| {member.member_email:<15}| {member.member_status.value:<15}\n")
    return

def advanced_search():
    print("~~~~ Function ~~~~")
    pass

#=-= Borrowing Feature Menu Functions =-=
def get_borrowing(connection, required:bool) -> Borrowing | None:
    borrowing_id = get_id("member",required)

    borrowing = storage.get_borrowing_from_database(
        connection,
        borrowing_id
    )
    return borrowing if borrowing is not None else None

def borrow_book(connection) -> bool:
    print("~~~~ Borrow a Book Function ~~~~")

    # Get Member First
    member = get_member(connection, required=False)
    if member is None:
        return
    elif member.member_status == "Inactive":
        print("Not Eligible to Borrow, Status Member Inactive.\n")
        return

    while True:
    #wrap in while true for condition if book desired isnt available
        # member is not None, get book next
        book_to_borrow = get_book(connection, required=False)
        if book_to_borrow is None:
            print("Cancelling Borrow Book")
            return

        # book is not None, check availability
        if not book_to_borrow.available :
            print("Book is not available to borrow, choose another book")
            continue
        else:
            #else available, get current date
            borrow_date = get_current_date()
            borrowing_id = get_id("borrowing")
            

            new_borrowing = Borrowing(
                borrowing_id=borrowing_id,
                member_id=member.member_id,
                book_id=book_to_borrow.book_id,
                borrow_date=borrow_date,
                return_date=None
            )
            storage.insert_borrowing_into_database(connection, new_borrowing)
            storage.update_book_availability_in_database(connection, book_to_borrow.book_id, False)
            storage.display_borrowing_given_id(connection, new_borrowing.borrowing_id)
            print("New Borrowing Entry has been Added.\n")
            break

# to return book
def return_book(connection) -> bool:
    print("~~~~ Function ~~~~")
    #get borrowing object from database
    borrowing = get_borrowing(connection, False)
    if borrowing is None:
        return

    #check if return date is filled or not
    if borrowing.return_date is not None:
        print("Book already returned")
        return

    #update availability to true(available)
    book = storage.get_book_from_database(connection, borrowing.book_id)
    storage.update_book_availability_in_database(connection, True)

    #update return_date to current date
    return_date = datetime.now().date()
    borrowing.return_date = return_date

    #update database
    storage.update_borrowing_in_database(connection, borrowing)
    storage.display_borrowing_given_id(connection, borrowing_id=borrowing.borrowing_id)
    return True

#get the books borrowed by a member
def display_member_borrowed_books(connection) -> None:
    print("~~~~ Member Borrowed Book Function ~~~~")
    member = get_member(connection, required=False)

    if member is not None:
        storage.display_member_borrowing(connection, member)
    return

#=-= Book Management Menu Functions =-=
def get_book(connection, required:bool) -> Book | None:
    book_id = get_id("book",required)

    book = storage.get_book_from_database(connection,book_id)

    return book if book is not None else None

#Function to add a book object
def add_book(connection) -> None:
    print("~~~~ Add a Book Function ~~~~")
    while True:
        book_id = get_id("book",required=True)
        if storage.book_exists(connection, book_id):
            print("Book already exists")
            continue
        break

    title = get_title()
    authors = get_authors_sequence(connection)
    publisher = get_publisher(connection,required=False)
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
        connection
) -> bool:
    print("~~~~ Update a Book Function ~~~~")

    while True:
        book_id = get_id("book",required=False)
        if book_id is None:
            return False
        elif not storage.book_exists(connection, book_id):
            print("Book Not Found")
            continue
        else:
            storage.display_book_with_given_id(connection,book_id)
            book = storage.get_book_from_database(connection,book_id)
            break

    while True:
        print("""
        ┌──────────────────────────────┐
        │       UPDATE BOOK MENU       │
        ├──────────────────────────────┤
        │ 1. Title                     │
        │ 2. Authors                   │
        │ 3. Publisher                 │
        │ 4. Categories                │
        │ 5. Published Date            │
        │ 0. Done                      │
        └──────────────────────────────┘
        """)

        choice = input("Input Menu (number): ").strip()
        if choice == "1":
            updated_title = get_title()
            storage.update_book_in_database(connection, book, title=updated_title)
        elif choice == "2":
            updated_authors = get_authors_sequence(connection)
            storage.update_book_in_database(connection, book, authors=updated_authors)
        elif choice == "3":
            updated_publisher = get_publisher(connection, required=False)
            storage.update_book_in_database(connection, book, publisher=updated_publisher)
        elif choice == "4":
            updated_categories = get_categories_sequence(connection)
            storage.update_book_in_database(connection, book, categories=updated_categories)
        elif choice == "5":
            updated_published_date = get_published_date()
            storage.update_book_in_database(connection, book, published_date=updated_published_date)
        elif choice == "0":
            return
        else:
            print("INVALID MENU")

#to delete a book, returns True if exists and deleted, else False
def delete_book(connection, book_id: str) -> bool:
    print("~~~~ Delete a Book Function ~~~~")
    while True:
        book_id = get_id("book",required=False)
        if book_id is None:
            return False
        elif not storage.book_exists(connection, book_id):
            print("Book Not Found")
            continue
        else:
            storage.display_book_with_given_id(connection,book_id)
            break
    return storage.delete_book_from_database(connection, book_id)


def view_all_books(connection):
    print("~~~~ View All Books Function ~~~~")
    books = storage.fetch_all_books_from_database(connection)

    if not books :
        print("No Books in Database")
        return
    
    for book in books:
        authors = ", ".join(author.author_name for author in book.authors)
        categories = ", ".join(category for category in book.categories)
        publisher = book.publisher
        if publisher == None:
            publisher_name = "None"
        else:
            publisher_name = book.publisher.publisher_name
        print(f"{book.book_id}| {book.title:<30}| {authors:<25}| {publisher_name:<25}| {categories:<25}| {book.available:<10}| {str(book.published_date):<15}")

def view_book(connection):
    print("~~~~ View A Book Function ~~~~")
    while True:
        book_id = get_id("book",required=False)
        if book_id is None:
            return False
        elif not storage.book_exists(connection, book_id):
            print("Book Not Found")
            continue
        else:
            storage.display_book_with_given_id(connection,book_id)
            return
        
#get category sequence
def get_categories_sequence(connection):
    category_list = []
    while True:
        view_all_categories(connection)
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
        view_all_authors(connection)
        author_id = get_id("author",required=False)
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
        
def view_all_categories(connection):
    categories = storage.fetch_all_categories(connection)
    if categories is None:
        print("No Categories Found")

    for category_id, category_name in categories.items():
        print(f"{category_id:<10} : {category_name}")
