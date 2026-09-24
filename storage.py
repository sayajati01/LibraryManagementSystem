from pathlib import Path
from models import Book,Author,Publisher,Member,Borrowing,Category,MemberStatus
from datetime import date
import sqlite3

DATA_FILE = Path(__file__).parent / "library.db"


# ========= LIBRARY MANAGEMENT FUNCTION =========
def create_tables_publishers(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id TEXT PRIMARY KEY,
            publisher_name TEXT NOT NULL,
            publisher_city TEXT NOT NULL
        )
    """)

def create_tables_authors(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id TEXT PRIMARY KEY,
            author_name TEXT NOT NULL
        )
    """)

def create_tables_members(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id TEXT PRIMARY KEY,
            member_name TEXT NOT NULL,
            member_email TEXT NOT NULL,
            member_status TEXT NOT NULL
        )
    """)

def create_tables_books(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books_new (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            publisher_id TEXT,
            available INTEGER NOT NULL DEFAULT 1,
            published_date TEXT NOT NULL,

        FOREIGN KEY (publisher_id)
            REFERENCES publishers(publisher_id)
        )
    """)

def create_tables_categories(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id TEXT PRIMARY KEY,
            category_name TEXT NOT NULL UNIQUE
        )
    """)

def create_tables_book_categories(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_categories (
            book_id TEXT NOT NULL,
            category_id TEXT NOT NULL,

            PRIMARY KEY (book_id, category_id),

            FOREIGN KEY (book_id)
                REFERENCES books(book_id),
            
            FOREIGN KEY( category_id)
                REFERENCES categories(category_id)        
        
        )
    """)
    
def create_tables_book_authors(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_authors (
            book_id TEXT NOT NULL,
            author_id TEXT NOT NULL,

            PRIMARY KEY (book_id, author_id),

            FOREIGN KEY (book_id)
                REFERENCES books(book_id),
            
            FOREIGN KEY (author_id)
                REFERENCES authors(author_id)
        )
    """)
    
def create_tables_borrowings(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowings (
            borrowing_id TEXT PRIMARY KEY,
            member_id TEXT NOT NULL,
            book_id TEXT NOT NULL,
            borrow_date TEXT NOT NULL,
            return_date TEXT,

        FOREIGN KEY (member_id)
            REFERENCES members(member_id)
        
        FOREIGN KEY (book_id)
            REFERENCES books(book_id)
        )
    """)

def create_tables(connection):
    create_tables_publishers(connection)
    create_tables_authors(connection)
    create_tables_members(connection)
    create_tables_books(connection)
    create_tables_categories(connection)
    create_tables_book_authors(connection)
    create_tables_book_categories(connection)
    create_tables_borrowings(connection)

    connection.commit()

def get_borrowed_books_of_a_member_from_database(member_id:str) -> list[Book]:
    return

# ===-=== ===-=== ===-===
#
# Publisher Focused 
#
# ===-=== ===-=== ===-===
def publisher_exists (connection, publisher_id) -> bool :
    cursor = connection.cursor()
    cursor.execute("""
        SELECT publisher_id
        FROM publishers
        WHERE publisher_id = ?
    """,(publisher_id,))

    return cursor.fetchone() is not None

def insert_publisher_to_database(connection, publisher : Publisher) -> None:
    cursor = connection.cursor()

    if publisher_exists(connection, publisher.publisher_id):
        print("Publisher Exists")
        return
    
    cursor.execute("""
        INSERT OR IGNORE INTO publishers (
            publisher_id, 
            publisher_name,
            publisher_city
        )
        VALUES ( ? ,? ,?)
    """, (
        publisher.publisher_id,
        publisher.publisher_name,
        publisher.publisher_city
    ))
    connection.commit()

def get_publisher_from_database(connection, publisher_id : str) -> Publisher | None:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT publisher_id, publisher_name, publisher_city
        FROM publishers
        WHERE publisher_id = ?
    """, (
        publisher_id,
    ))

    row = cursor.fetchone()

    if row is None:
        return None
    
    publisher = Publisher(
        publisher_id=row[0],
        publisher_name=row[1],
        publisher_city=row[2]
    )

    return publisher

def update_publisher_in_database(
        connection,
        publisher_id:str,
        new_publisher_name:str,
        new_publisher_city:str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE publishers
        SET publisher_name = ?,
            publisher_city = ?
        WHERE publisher_id = ?
    """, (
        new_publisher_name,
        new_publisher_city,
        publisher_id
    )) 

    connection.commit()
    return cursor.rowcount > 0

def delete_publisher_from_database(
        connection,
        publisher_id:str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM publishers
        WHERE publisher_id = ?
    """, (
        publisher_id,
    ))
    connection.commit()
    return cursor.rowcount > 0

def fetch_all_publishers_from_database(connection) -> list[Publisher]:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT publisher_id, publisher_name, publisher_city
        FROM publishers
    """)

    rows = cursor.fetchall()
    publishers = []

    for row in rows:
        publisher = Publisher(
            publisher_id = row[0],
            publisher_name = row[1],
            publisher_city = row[2]
        )
        publishers.append(publisher)
    return publishers

def display_publisher_with_given_id(connection, publisher_id: str) -> None:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT publisher_id, publisher_name, publisher_city
        FROM publishers
        WHERE publisher_id = ?
    """, (publisher_id,))

    row = cursor.fetchone()

    print(f"Publisher ID   : {row[0]}")
    print(f"Publisher Name : {row[1]}")
    print(f"Publisher City : {row[2]}")

# ===-===  ===-===  ===-===
# 
# AUTHOR FOCUSED 
# 
# ===-=== ===-=== ===-===
def author_exists (connection, author_id) -> bool :
    cursor = connection.cursor()
    cursor.execute("""
        SELECT author_id
        FROM authors
        WHERE author_id = ?
    """,(author_id,))

    return cursor.fetchone() is not None

def insert_author_to_database(connection, author : Author) -> None:
    cursor = connection.cursor()

    if author_exists(connection, author.author_id):
        print("Author Exists")
        return
    
    cursor.execute("""
        INSERT INTO authors (
            author_id, author_name
        ) 
        VALUES ( ? ,? )
    """, (
        author.author_id , 
        author.author_name
    ))
    connection.commit()    

def get_author_from_database(connection, author_id : str) -> Author | None:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT author_id, author_name
        FROM authors
        WHERE author_id = ?
    """, (
        author_id,
    ))

    row = cursor.fetchone()

    if row is None :
        return None
    
    author = Author(
        author_id=row[0],
        author_name=row[1]
    )

    return author

def update_author_in_database(
        connection,
        author_id:str,
        new_author_name:str,
    ) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE authors
        SET author_name = ?
        WHERE author_id = ?
    """,(
        new_author_name,
        author_id
    ))

    connection.commit()
    return cursor.rowcount > 0

def delete_author_from_database(
        connection,
        author_id:str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM authors
        WHERE author_id = ?
    """, (
        author_id,
    ))
    connection.commit()
    return cursor.rowcount > 0

def fetch_all_authors_from_database(
        connection
) -> list[Author] :
    cursor = connection.cursor()
    cursor.execute("""
        SELECT author_id, author_name
        FROM authors
    """)

    rows = cursor.fetchall()
    author_list = []

    for row in rows :
        author = Author(
            author_id = row[0],
            author_name = row[1]
        )
        author_list.append(author)

    return author_list

def display_author_with_given_id(connection, author_id: str) -> None:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT author_id, author_name
        FROM authors
        WHERE author_id = ?
    """, (author_id,))

    row = cursor.fetchone()

    print(f"Author ID   : {row[0]}")
    print(f"Author Name : {row[1]}")
    


# ===-===  ===-=== ===-===
# 
# MEMBER FOCUSED
# 
# ===-=== ===-=== ===-===
def member_exists(connection, member_id) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT member_id
        FROM members
        WHERE member_id = ?
    """,(member_id,))

    return cursor.fetchone() is not None

def insert_member_to_database(connection, member:Member) -> None:
    cursor = connection.cursor()

    if member_exists(connection, member.member_id):
        print("Member Exists")
        return
    
    cursor.execute("""
        INSERT INTO members (
            member_id,
            member_name,
            member_email,
            member_status
        ) 
        VALUES ( ? ,? ,?, ?)
    """, (
        member.member_id , 
        member.member_name,
        member.member_email,
        member.member_status.value
    ))
    connection.commit()
    
def get_member_from_database(connection, member_id : str) -> Member | None:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT member_id, member_name, member_email, member_status
        FROM members
        WHERE member_id = ?
    """, (
        member_id,
    ))

    row = cursor.fetchone()

    if row is None:
        return None

    member = Member(
        member_id=row[0],
        member_name=row[1],
        member_email=row[2],
        member_status=MemberStatus(row[3])
    )

    return member

def update_member_in_database(
        connection,
        member_id : str,
        updated_name : str,
        updated_email : str,
        updated_status : str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE members
        SET member_name = ?,
            member_email = ?,
            member_status = ?
        WHERE member_id = ?
    """, (
        updated_name,
        updated_email,
        updated_status,
        member_id
    ))

    connection.commit()
    return cursor.rowcount > 0

def delete_member_from_database(
        connection,
        member_id:str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM members
        WHERE member_id = ?
    """, (
        member_id,
    ))
    connection.commit()
    return cursor.rowcount > 0

def fetch_all_members_from_database(
        connection
) -> list[Member]:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT member_id, member_name, member_email, member_status
        FROM members
    """)

    rows = cursor.fetchall()
    members = []

    for row in rows :
        member = Member(
            member_id=row[0],
            member_name=row[1],
            member_email=row[2],
            member_status=MemberStatus(row[3])
        )
        members.append(member)

    return members

def display_member_with_given_id(connection, member_id: str) -> None:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT member_id, member_name, member_email, member_status
        FROM members
        WHERE member_id = ?
    """, (member_id,))

    row = cursor.fetchone()

    print(f"Member ID     : {row[0]}")
    print(f"Member Name   : {row[1]}")
    print(f"Member Email  : {row[2]}")
    print(f"Member Status : {row[3]}")

# -=-=- Category? =-=-=-=
def generate_category_id(sequence) -> str:
    prefix = "CAT"
    end = f"{sequence:04d}"

    return prefix+end

def category_exists(connection, category_id) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category_id
        FROM categories
        WHERE category_id = ?
    """,(category_id,))

    return cursor.fetchone() is not None

def get_category_from_database(connection, category_id) -> Category:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category_name
        FROM categories
        WHERE category_id = ?
    """,(
        category_id,
    ))

    row = cursor.fetchone()
    return row[0]

def fetch_all_categories(
        connection
) -> dict:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category_id, category_name
        FROM categories
    """)

    rows = cursor.fetchall()
    if rows is None:
        return None
    
    categories = {}
    for row in rows:
        categories[row[0]] = row[1]

    return categories

def insert_category_into_db(connection) -> None :
    cursor = connection.cursor()

    for sequence,category in enumerate(Category, start=1):
        category_id = generate_category_id(sequence)

        if category_exists(connection, category_id):
            continue

        cursor.execute ("""
            INSERT INTO categories (category_id, category_name)
            VALUES (? ,?)
        """,(
            category_id, category.value
        ))
        connection.commit()
    return

# ===-=== BOOK_CATEGORIES TABLE ===-====
def insert_book_and_corresponding_authors_into_database(
        connection, 
        book_id:str, 
        authors:list[Author]
    ) -> None:
    cursor = connection.cursor()
    for author in authors:
        cursor.execute("""
            INSERT INTO book_authors(
                book_id,
                author_id
            )
            VALUES (?,?)
        """,(
            book_id,
            author.author_id
        ))
    connection.commit()

# ===-=== BOOK_AUTHORS TABLE ===-===
def insert_book_and_corresponding_categories_into_database(
        connection,
        book_id:str,
        categories:list[Category]
) -> None:
    cursor = connection.cursor()
    for category in categories:
        cursor.execute("""
            SELECT category_id
            FROM categories
            WHERE category_name = ?
        """,(
            category,
        ))
        row = cursor.fetchone()
        category_id = row[0]
        cursor.execute("""
            INSERT INTO book_categories (
                book_id,
                category_id
            )

            VALUES (?,?)
        """,(
            book_id,
            category_id
        ))

    connection.commit()


# ===-=== BOOK FOCUSED ===-===
def get_book_from_database(connection, book_id: str) -> Book | None:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT book_id, title, publisher_id, available, published_date
        FROM books
        WHERE book_id = ?
    """, (book_id,))

    row = cursor.fetchone()

    if row is None:
        return None

    # Publisher
    publisher = None

    if row[2] is not None:
        publisher = get_publisher_from_database(
            connection,
            row[2]
        )

    # Authors
    cursor.execute("""
        SELECT author_id
        FROM book_authors
        WHERE book_id = ?
    """, (book_id,))

    author_rows = cursor.fetchall()

    authors = []

    for author_row in author_rows:
        author = get_author_from_database(
            connection,
            author_row[0]
        )

        if author is not None:
            authors.append(author)

    # Categories
    cursor.execute("""
        SELECT category_id
        FROM book_categories
        WHERE book_id = ?
    """, (book_id,))

    category_rows = cursor.fetchall()

    categories = []

    for category_row in category_rows:
        category = get_category_from_database(
            connection,
            category_row[0]
        )

        if category is not None:
            categories.append(category)

    # Reconstruct Book
    book = Book(
        book_id=row[0],
        title=row[1],
        author=authors,
        publisher=publisher,
        category=categories,
        available=bool(row[3]),
        published_date=date.fromisoformat(row[4])
    )

    return book

def book_exists(connection, book_id) -> bool:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT book_id
        FROM books
        WHERE book_id = ?
    """, (book_id,))

    return cursor.fetchone() is not None

def insert_book_into_database(
        connection,
        book:Book
    ) -> None :
    cursor = connection.cursor()

    if book_exists(connection, book.book_id) :
        print("Book already exists")
        return

    publisher_id = None
    if book.publisher is not None :
        publisher_id = book.publisher.publisher_id

    cursor.execute("""
        INSERT INTO books (book_id, title, publisher_id, available, published_date)
        VALUES (?,?,?,?,?)
    """,(
        book.book_id,
        book.title,
        publisher_id,
        book.available,
        str(book.published_date)
    ))

    connection.commit()

def fetch_all_books_from_database(connection) -> list[Book]:
    cursor = connection.cursor()

    # Get all books
    cursor.execute("""
        SELECT book_id, title, publisher_id, available, published_date
        FROM books
    """)

    book_rows = cursor.fetchall()

    books = []

    for book_row in book_rows:
        book_id = book_row[0]
        title = book_row[1]
        publisher_id = book_row[2]
        available = bool(book_row[3])
        published_date = date.fromisoformat(book_row[4])

        # Get publisher
        publisher = None

        if publisher_id is not None:
            publisher = get_publisher_from_database(
                connection,
                publisher_id
            )

        # Get authors
        cursor.execute("""
            SELECT author_id
            FROM book_authors
            WHERE book_id = ?
        """, (book_id,))

        author_rows = cursor.fetchall()

        authors = []

        for author_row in author_rows:
            author_id = author_row[0]

            author = get_author_from_database(
                connection,
                author_id
            )

            if author is not None:
                authors.append(author)

        # Get categories
        cursor.execute("""
            SELECT category_id
            FROM book_categories
            WHERE book_id = ?
        """, (book_id,))

        category_rows = cursor.fetchall()

        categories = []

        for category_row in category_rows:
            category_id = category_row[0]

            category = get_category_from_database(
                connection,
                category_id
            )

            if category is not None:
                categories.append(category)

        # Reconstruct Book object
        book = Book(
            book_id=book_id,
            title=title,
            authors=authors,
            publisher=publisher,
            categories=categories,
            available=available,
            published_date=published_date
        )

        books.append(book)

    return books

def update_book_in_database(
        connection,
        book:Book,
        title:str | None,
        authors:list[Author] | None,
        publisher:Publisher | None,
        categories:list[Category] | None,
        published_date:date | None
    ) -> bool:
    cursor = connection.cursor()
    book_id = book.book_id
    if title is not None:
        #title is in table books
        cursor.execute("""
            UPDATE books
            SET title = ?
            WHERE book_id = ?
        """,( 
            title,
            book_id
        ))
    if authors is not None:
        cursor.execute("""
            DELETE FROM book_authors
            WHERE book_id = ?
        """,( 
            book_id,
        ))
        for author in authors:
            cursor.execute("""
                INSERT INTO book_authors (book_id, author_id)
                VALUES (?,?)
            """,( 
                book_id,
                author.author_id
            ))
        
    if publisher is not None:
        cursor.execute("""
            UPDATE books
            SET publisher_id = ?
            WHERE book_id = ?
        """,( 
            publisher.publisher_id,
            book_id
        ))
        
    if categories is not None:
        cursor.execute("""
            DELETE FROM book_categories
            WHERE book_id = ?
        """,( 
            book_id,
        ))
        for category in categories:
            cursor.execute("""
                SELECT category_id
                FROM categories
                WHERE category_name = ?
            """,(
                category,
            ))
            row = cursor.fetchone()
            category_id = row[0]
            cursor.execute("""
                INSERT INTO book_categories (
                    book_id,
                    category_id
                )
    
                VALUES (?,?)
            """,(
                book_id,
                category_id
            ))
        
    if published_date is not None:
        cursor.execute("""
            UPDATE books
            SET published_date = ?
            WHERE book_id = ?
        """,( 
            str(published_date),
            book_id
        ))
        

    connection.commit()
    display_book_with_given_id(connection, book.book_id)
    return True

def get_books_by_criteria_from_database(
) -> list[Book] | None:
    return

def update_book_availability_in_database(book_id: str, available: bool) -> None:
    return

def delete_book_from_database(book_id: str) -> bool:
    return

def check_book_exists_in_database(book_id: str) -> bool:
    return

def display_book_with_given_id(connection, book_id: str) -> None:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT book_id, title, publisher_id, available, published_date
        FROM books
        WHERE book_id = ?
    """, (book_id,))

    row = cursor.fetchone()

    print(f"Book ID         : {row[0]}")
    print(f"Title           : {row[1]}")

    # Publisher
    if row[2] is not None:
        publisher = get_publisher_from_database(connection, row[2])
        print(f"Publisher       : {publisher.publisher_name}")
    else:
        print("Publisher       : None")

    # Authors
    cursor.execute("""
        SELECT author_id
        FROM book_authors
        WHERE book_id = ?
    """, (book_id,))

    author_rows = cursor.fetchall()

    print("Authors         :")

    if author_rows:
        for author_row in author_rows:
            author = get_author_from_database(
                connection,
                author_row[0]
            )
            print(f"  - {author.author_name}")
    else:
        print("  - None")

    # Categories
    cursor.execute("""
        SELECT category_id
        FROM book_categories
        WHERE book_id = ?
    """, (book_id,))

    category_rows = cursor.fetchall()

    print("Categories      :")

    if category_rows:
        for category_row in category_rows:
            category = get_category_from_database(
                connection,
                category_row[0]
            )
            print(f"  - {category}")
    else:
        print("  - None")

    print(f"Available       : {bool(row[3])}")
    print(f"Published Date  : {row[4]}")


# === sql function ===
def create_connection():
    connection = sqlite3.connect("library.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection