import sqlite3
import unittest
from datetime import date

import storage
from models import (
    Author,
    Publisher,
    Member,
    MemberStatus,
    Book,
    Borrowing,
)


class StorageTestCase(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute("PRAGMA foreign_keys = ON")

        storage.create_tables_authors(self.connection)
        storage.create_tables_publishers(self.connection)
        storage.create_tables_members(self.connection)
        storage.create_tables_categories(self.connection)
        storage.create_tables_books(self.connection)
        storage.create_tables_book_authors(self.connection)
        storage.create_tables_book_categories(self.connection)
        storage.create_tables_borrowings(self.connection)

        storage.insert_category_into_db(self.connection)

    def tearDown(self):
        self.connection.close()

    def create_publisher(self):
        publisher = Publisher(
            "PUB20260001",
            "Penguin Books",
            "London"
        )

        storage.insert_publisher_to_database(
            self.connection,
            publisher
        )

        return publisher

    def create_author(self):
        author = Author(
            "AUT20260001",
            "George Orwell"
        )

        storage.insert_author_to_database(
            self.connection,
            author
        )

        return author

    def create_member(self):
        member = Member(
            "MEM20260001",
            "Alice Johnson",
            "alice@example.com",
            MemberStatus.ACTIVE
        )

        storage.insert_member_to_database(
            self.connection,
            member
        )

        return member

    def create_book(self):
        publisher = self.create_publisher()
        author = self.create_author()

        book = Book(
            book_id="BOOK20260001",
            title="1984",
            authors=[author],
            publisher=publisher,
            categories=["Fiction"],
            available=True,
            published_date=date(1949, 6, 8)
        )

        storage.insert_book_into_database(
            self.connection,
            book
        )

        storage.insert_book_and_corresponding_authors_into_database(
            self.connection,
            book.book_id,
            book.authors
        )

        storage.insert_book_and_corresponding_categories_into_database(
            self.connection,
            book.book_id,
            book.categories
        )

        return book
class TestPublisherStorage(StorageTestCase):

    def test_publisher_exists_false(self):
        self.assertFalse(
            storage.publisher_exists(
                self.connection,
                "PUB20260001"
            )
        )

    def test_insert_and_get_publisher(self):
        publisher = self.create_publisher()

        result = storage.get_publisher_from_database(
            self.connection,
            publisher.publisher_id
        )

        self.assertEqual(
            result,
            publisher
        )

    def test_publisher_exists_after_insert(self):
        publisher = self.create_publisher()

        self.assertTrue(
            storage.publisher_exists(
                self.connection,
                publisher.publisher_id
            )
        )

    def test_update_publisher(self):
        publisher = self.create_publisher()

        result = storage.update_publisher_in_database(
            self.connection,
            publisher.publisher_id,
            "HarperCollins",
            "New York"
        )

        self.assertTrue(result)

        updated = storage.get_publisher_from_database(
            self.connection,
            publisher.publisher_id
        )

        self.assertEqual(
            updated.publisher_name,
            "HarperCollins"
        )

        self.assertEqual(
            updated.publisher_city,
            "New York"
        )

    def test_delete_publisher(self):
        publisher = self.create_publisher()

        result = storage.delete_publisher_from_database(
            self.connection,
            publisher.publisher_id
        )

        self.assertTrue(result)

        self.assertIsNone(
            storage.get_publisher_from_database(
                self.connection,
                publisher.publisher_id
            )
        )

    def test_fetch_all_publishers(self):
        self.create_publisher()

        publishers = storage.fetch_all_publishers_from_database(
            self.connection
        )

        self.assertEqual(len(publishers), 1)

class TestAuthorStorage(StorageTestCase):

    def test_author_exists(self):
        self.assertFalse(
            storage.author_exists(
                self.connection,
                "AUT20260001"
            )
        )

        author = self.create_author()

        self.assertTrue(
            storage.author_exists(
                self.connection,
                author.author_id
            )
        )

    def test_insert_and_get_author(self):
        author = self.create_author()

        result = storage.get_author_from_database(
            self.connection,
            author.author_id
        )

        self.assertEqual(result, author)

    def test_update_author(self):
        author = self.create_author()

        result = storage.update_author_in_database(
            self.connection,
            author.author_id,
            "Jane Austen"
        )

        self.assertTrue(result)

        updated = storage.get_author_from_database(
            self.connection,
            author.author_id
        )

        self.assertEqual(
            updated.author_name,
            "Jane Austen"
        )

    def test_delete_author(self):
        author = self.create_author()

        result = storage.delete_author_from_database(
            self.connection,
            author.author_id
        )

        self.assertTrue(result)

        self.assertIsNone(
            storage.get_author_from_database(
                self.connection,
                author.author_id
            )
        )

    def test_fetch_all_authors(self):
        self.create_author()

        authors = storage.fetch_all_authors_from_database(
            self.connection
        )

        self.assertEqual(len(authors), 1)
class TestMemberStorage(StorageTestCase):

    def test_member_exists(self):
        self.assertFalse(
            storage.member_exists(
                self.connection,
                "MEM20260001"
            )
        )

        member = self.create_member()

        self.assertTrue(
            storage.member_exists(
                self.connection,
                member.member_id
            )
        )

    def test_insert_and_get_member(self):
        member = self.create_member()

        result = storage.get_member_from_database(
            self.connection,
            member.member_id
        )

        self.assertEqual(result, member)

    def test_update_member(self):
        member = self.create_member()

        result = storage.update_member_in_database(
            self.connection,
            member.member_id,
            "Bob Williams",
            "bob@example.com",
            "Inactive"
        )

        self.assertTrue(result)

        updated = storage.get_member_from_database(
            self.connection,
            member.member_id
        )

        self.assertEqual(
            updated.member_name,
            "Bob Williams"
        )

        self.assertEqual(
            updated.member_email,
            "bob@example.com"
        )

        self.assertEqual(
            updated.member_status,
            MemberStatus.INACTIVE
        )

    def test_delete_member(self):
        member = self.create_member()

        result = storage.delete_member_from_database(
            self.connection,
            member.member_id
        )

        self.assertTrue(result)

        self.assertIsNone(
            storage.get_member_from_database(
                self.connection,
                member.member_id
            )
        )

class TestBookStorage(StorageTestCase):

    def test_book_exists(self):
        self.assertFalse(
            storage.book_exists(
                self.connection,
                "BOOK20260001"
            )
        )

        book = self.create_book()

        self.assertTrue(
            storage.book_exists(
                self.connection,
                book.book_id
            )
        )

    def test_get_book(self):
        book = self.create_book()

        result = storage.get_book_from_database(
            self.connection,
            book.book_id
        )

        self.assertEqual(
            result.book_id,
            book.book_id
        )

        self.assertEqual(
            result.title,
            book.title
        )

        self.assertEqual(
            result.authors,
            book.authors
        )

        self.assertEqual(
            result.publisher,
            book.publisher
        )

        self.assertEqual(
            result.categories,
            book.categories
        )

    def test_get_nonexistent_book(self):
        result = storage.get_book_from_database(
            self.connection,
            "BOOK20269999"
        )

        self.assertIsNone(result)

    def test_fetch_all_books(self):
        self.create_book()

        books = storage.fetch_all_books_from_database(
            self.connection
        )

        self.assertEqual(len(books), 1)

    def test_update_book_title(self):
        book = self.create_book()

        result = storage.update_book_in_database(
            self.connection,
            book,
            title="Animal Farm"
        )

        self.assertTrue(result)

        updated = storage.get_book_from_database(
            self.connection,
            book.book_id
        )

        self.assertEqual(
            updated.title,
            "Animal Farm"
        )

    def test_update_book_availability(self):
        book = self.create_book()

        storage.update_book_availability_in_database(
            self.connection,
            book.book_id,
            False
        )

        updated = storage.get_book_from_database(
            self.connection,
            book.book_id
        )

        self.assertFalse(
            updated.available
        )

    def test_update_book_authors(self):
        book = self.create_book()

        second_author = Author(
            "AUT20260002",
            "Jane Austen"
        )

        storage.insert_author_to_database(
            self.connection,
            second_author
        )

        storage.update_book_in_database(
            self.connection,
            book,
            authors=[second_author]
        )

        updated = storage.get_book_from_database(
            self.connection,
            book.book_id
        )

        self.assertEqual(
            updated.authors,
            [second_author]
        )

    def test_update_book_categories(self):
        book = self.create_book()

        storage.update_book_in_database(
            self.connection,
            book,
            categories=["Mystery"]
        )

        updated = storage.get_book_from_database(
            self.connection,
            book.book_id
        )

        self.assertEqual(
            updated.categories,
            ["Mystery"]
        )
class TestBorrowingStorage(StorageTestCase):

    def test_insert_and_get_borrowing(self):
        member = self.create_member()
        book = self.create_book()

        borrowing = Borrowing(
            borrowing_id="BOR20260001",
            member_id=member.member_id,
            book_id=book.book_id,
            borrow_date=date(2026, 9, 25),
            return_date=None
        )

        result = storage.insert_borrowing_into_database(
            self.connection,
            borrowing
        )

        self.assertTrue(result)

        stored = storage.get_borrowing_from_database(
            self.connection,
            borrowing.borrowing_id
        )

        self.assertEqual(
            stored.borrowing_id,
            borrowing.borrowing_id
        )

        self.assertEqual(
            stored.member_id,
            borrowing.member_id
        )

        self.assertEqual(
            stored.book_id,
            borrowing.book_id
        )

        self.assertEqual(
            stored.borrow_date,
            borrowing.borrow_date
        )

        self.assertIsNone(
            stored.return_date
        )

    def test_get_nonexistent_borrowing(self):
        result = storage.get_borrowing_from_database(
            self.connection,
            "BOR20269999"
        )

        self.assertIsNone(result)

    def test_update_return_date(self):
        member = self.create_member()
        book = self.create_book()

        borrowing = Borrowing(
            "BOR20260001",
            member.member_id,
            book.book_id,
            date(2026, 9, 20),
            None
        )

        storage.insert_borrowing_into_database(
            self.connection,
            borrowing
        )

        borrowing.return_date = date(2026, 9, 25)

        storage.update_borrowing_in_database(
            self.connection,
            borrowing
        )

        stored = storage.get_borrowing_from_database(
            self.connection,
            borrowing.borrowing_id
        )

        self.assertEqual(
            stored.return_date,
            date(2026, 9, 25)
        )