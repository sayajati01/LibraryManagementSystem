import unittest
from datetime import date

from models import (
    Author,
    Publisher,
    Member,
    MemberStatus,
    Category,
    Book,
    Borrowing,
)


class TestPublisher(unittest.TestCase):

    def test_publisher_creation(self):
        publisher = Publisher(
            publisher_id="PUB20260001",
            publisher_name="Penguin Books",
            publisher_city="London"
        )

        self.assertEqual(publisher.publisher_id, "PUB20260001")
        self.assertEqual(publisher.publisher_name, "Penguin Books")
        self.assertEqual(publisher.publisher_city, "London")


class TestAuthor(unittest.TestCase):

    def test_author_creation(self):
        author = Author(
            author_id="AUT20260001",
            author_name="George Orwell"
        )

        self.assertEqual(author.author_id, "AUT20260001")
        self.assertEqual(author.author_name, "George Orwell")


class TestMember(unittest.TestCase):

    def test_member_creation(self):
        member = Member(
            member_id="MEM20260001",
            member_name="Alice Johnson",
            member_email="alice@example.com",
            member_status=MemberStatus.ACTIVE
        )

        self.assertEqual(member.member_id, "MEM20260001")
        self.assertEqual(member.member_name, "Alice Johnson")
        self.assertEqual(member.member_email, "alice@example.com")
        self.assertEqual(member.member_status, MemberStatus.ACTIVE)


class TestMemberStatus(unittest.TestCase):

    def test_status_values(self):
        self.assertEqual(MemberStatus.ACTIVE.value, "Active")
        self.assertEqual(MemberStatus.INACTIVE.value, "Inactive")


class TestCategory(unittest.TestCase):

    def test_category_values(self):
        self.assertEqual(Category.FICTION.value, "Fiction")
        self.assertEqual(Category.FANTASY.value, "Fantasy")
        self.assertEqual(Category.PSYCHOLOGY.value, "Psychology")


class TestBook(unittest.TestCase):

    def setUp(self):
        self.author = Author(
            "AUT20260001",
            "George Orwell"
        )

        self.publisher = Publisher(
            "PUB20260001",
            "Penguin Books",
            "London"
        )

        self.book = Book(
            book_id="BOOK20260001",
            title="1984",
            authors=[self.author],
            publisher=self.publisher,
            categories=["Fiction"],
            available=True,
            published_date=date(1949, 6, 8)
        )

    def test_book_creation(self):
        self.assertEqual(self.book.book_id, "BOOK20260001")
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.authors, [self.author])
        self.assertEqual(self.book.publisher, self.publisher)
        self.assertEqual(self.book.categories, ["Fiction"])
        self.assertTrue(self.book.available)
        self.assertEqual(
            self.book.published_date,
            date(1949, 6, 8)
        )

    def test_is_available_when_available(self):
        self.assertTrue(self.book.is_available())

    def test_is_available_when_unavailable(self):
        self.book.available = False

        self.assertFalse(self.book.is_available())


class TestBorrowing(unittest.TestCase):

    def test_borrowing_creation(self):
        borrowing = Borrowing(
            borrowing_id="BOR20260001",
            member_id="MEM20260001",
            book_id="BOOK20260001",
            borrow_date=date(2026, 9, 25),
            return_date=None
        )

        self.assertEqual(
            borrowing.borrowing_id,
            "BOR20260001"
        )
        self.assertEqual(
            borrowing.member_id,
            "MEM20260001"
        )
        self.assertEqual(
            borrowing.book_id,
            "BOOK20260001"
        )
        self.assertEqual(
            borrowing.borrow_date,
            date(2026, 9, 25)
        )
        self.assertIsNone(borrowing.return_date)


if __name__ == "__main__":
    unittest.main()