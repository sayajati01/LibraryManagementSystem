from pathlib import Path
from models import Book,Author,Publisher,Member,Borrowing
import sqlite3

DATA_FILE = Path(__file__).parent / "library.db"


# ========= LIBRARY MANAGEMENT FUNCTION =========
def create_tables_publisher(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id TEXT PRIMARY KEY,
            publisher_name TEXT NOT NULL,
            publisher_city TEXT NOT NULL
        )
    """)

def create_tables_author(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id TEXT PRIMARY KEY,
            author_name TEXT NOT NULL
        )
    """)

def create_tables_member(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_id TEXT PRIMARY KEY,
            member_name TEXT NOT NULL,
            member_email TEXT NOT NULL
        )
    """)

def create_tables_books(connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author_id TEXT NOT NULL,
            publisher_id TEXT NOT NULL,
            category TEXT NOT NULL,
            available INTEGER NOT NULL DEFAULT 1,
            published_date TEXT NOT NULL,

        FOREIGN KEY (author_id)
            REFERENCES authors(author_id)
        
        FOREIGN KEY (publisher_id)
            REFERENCES publishers(publisher_id)
        )
    """)

def create_tables_borrowing(connection) -> None:
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
    create_tables_publisher(connection)
    create_tables_author(connection)
    create_tables_member(connection)
    create_tables_books(connection)
    create_tables_borrowing(connection)

    connection.commit()

def get_borrowed_books_of_a_member_from_database(member_id:str) -> list[Book]:
    return

# ===-=== BOOK FOCUSED ===-===

def insert_book_to_database(book: Book) -> None:
    return

def update_book_in_database(
        book_id:str,
        title: str | None = None,
        author: Author | None = None,
        category: str | None = None,
    ) -> None:
    return

def get_books_by_criteria_from_database(
    book_id:str | None = None,
    year: int | None = None,
    month: int | None = None,
    author_name : str | None = None,
    category : str | None = None,
    publisher_id : str | None = None
) -> list[Book] | None:
    return

def update_book_availability_in_database(book_id: str, available: bool) -> None:
    return

def delete_book_from_database(book_id: str) -> bool:
    return

def check_book_exists_in_database(book_id: str) -> bool:
    return


# ===-=== ===-=== ===-===
#
# Publisher Focused 
#
# ===-=== ===-=== ===-===
def insert_publisher_to_database(connection, publisher : Publisher) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        INSER INTO publishers (
            publisher_id, 
            publisher_name,
            publisher_city
        )
        VALUES ( ? ,? ,?)
    """, (
        publisher.publisher_id,
        publisher.publisher_name,
        publisher.city
    ))

def get_publisher_from_database(connection, publisher_id : str) -> Publisher:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT publisher_id, publisher_name, publisher_city
        FROM publishers
        WHERE publisher_id = ?
    """, (
        publisher_id,
    ))

    row = cursor.fetchone()
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
            city = ?
        WHERE publisher_id = ?
    """, (
        new_publisher_name,
        new_publisher_city,
        publisher_id
    )) 

    connection.commit()
    return cursor.rowcount > 0

def delete_publisher_from_database():
    return

# ===-===  ===-===  ===-===
# 
# AUTHOR FOCUSED 
# 
# ===-=== ===-=== ===-===
def insert_author_to_database(connection, author : Author) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO authors (
            author_id, author_name
        ) 
        VALUES ( ? ,? )
    """, (
        author.author_id , 
        author.author_name
    ))    

def get_author_from_database(connection, author_id : str) -> Author:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT author_id, author_name
        FROM authors
        WHERE author_id = ?
    """, (
        author_id,
    ))

    row = cursor.fetchone()
    
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

def delete_author_from_database():
    return


# ===-===  ===-=== ===-===
# 
# MEMBER FOCUSED
# 
# ===-=== ===-=== ===-===
def insert_member_to_database(connection, member:Member) -> None:
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO members (
            member_id,
            member_name,
            member_email
        ) 
        VALUES ( ? ,? ,?)
    """, (
        member.member_id , 
        member.member_name,
        member.member_email
    ))
    
def get_member_from_database(connection, member_id : str) -> Member:
    cursor = connection.cursor()
    cursor.execute("""
        SELECT member_id, member_name, member_email
        FROM members
        WHERE member_id = ?
    """, (
        member_id,
    ))

    row = cursor.fetchone()
    member = Member(
        member_id=row[0],
        member_name=row[1],
        member_email=row[2]
    )

    return member

def update_member_in_database(
        connection,
        member_id : str,
        new_member_name : str,
        new_member_email : str
) -> bool:
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE members
        SET member.name = ?,
            member.email = ?
        WHERE member_id = ?
    """, (
        new_member_name,
        new_member_email,
        member_id
    ))

    connection.commit()
    return cursor.rowcount > 0

def delete_member_from_database():
    return

# === sql function ===
def create_connection():
    connection = sqlite3.connect("library.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection