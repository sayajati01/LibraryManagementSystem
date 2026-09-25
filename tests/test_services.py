import unittest
from unittest.mock import patch

from models import Book
from services import calculate_total_books
import services


class TestServiceCalculations(unittest.TestCase):

    def test_calculate_total_books(self):
        books = [
            object(),
            object(),
            object()
        ]

        result = calculate_total_books(books)

        self.assertEqual(result, 3)

    def test_calculate_total_books_empty(self):
        result = calculate_total_books([])

        self.assertEqual(result, 0)
        
class TestGetBook(unittest.TestCase):

    @patch("services.storage.get_book_from_database")
    @patch("services.get_id")
    def test_get_existing_book(
        self,
        mock_get_id,
        mock_get_book
    ):
        mock_get_id.return_value = "BOOK20260001"

        book = object()

        mock_get_book.return_value = book

        result = services.get_book(
            "fake_connection",
            required=False
        )

        self.assertIs(
            result,
            book
        )

        mock_get_id.assert_called_once_with(
            "book",
            False
        )

        mock_get_book.assert_called_once_with(
            "fake_connection",
            "BOOK20260001"
        )

    @patch("services.storage.get_book_from_database")
    @patch("services.get_id")
    def test_get_book_not_found(
        self,
        mock_get_id,
        mock_get_book
    ):
        mock_get_id.return_value = "BOOK20260001"
        mock_get_book.return_value = None

        result = services.get_book(
            "fake_connection",
            required=False
        )

        self.assertIsNone(result)
import services
from models import (
    Member,
    MemberStatus,
    Book,
    Borrowing
)
from datetime import date


class TestBorrowBook(unittest.TestCase):

    @patch("services.storage.display_borrowing_given_id")
    @patch("services.storage.update_book_availability_in_database")
    @patch("services.storage.insert_borrowing_into_database")
    @patch("services.get_id")
    @patch("services.get_current_date")
    @patch("services.get_book")
    @patch("services.get_member")
    def test_borrow_book_success(
        self,
        mock_get_member,
        mock_get_book,
        mock_get_current_date,
        mock_get_id,
        mock_insert,
        mock_update,
        mock_display
    ):
        member = Member(
            "MEM20260001",
            "Alice Johnson",
            "alice@example.com",
            MemberStatus.ACTIVE
        )

        book = Book(
            "BOOK20260001",
            "1984",
            [],
            None,
            [],
            True,
            date(1949, 6, 8)
        )

        mock_get_member.return_value = member
        mock_get_book.return_value = book
        mock_get_current_date.return_value = date(2026, 9, 25)
        mock_get_id.return_value = "BOR20260001"

        result = services.borrow_book("fake_connection")

        self.assertIsNone(result)

        mock_insert.assert_called_once()

        borrowing = mock_insert.call_args.args[1]

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

        mock_update.assert_called_once_with(
            "fake_connection",
            "BOOK20260001",
            False
        )