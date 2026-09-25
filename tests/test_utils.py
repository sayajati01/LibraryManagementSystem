import unittest
from datetime import date
from unittest.mock import patch

from models import Author, Book, Category, Publisher
from utils import (
    validate_id,
    validate_email,
    validate_name,
    validate_title,
    validate_author,
    validate_category,
    validate_published_date,
    validate_publisher,
    validate_city,
    validate_book,
    get_id,
    get_name,
    get_email,
    get_title,
    get_city,
    get_published_date,
)

class TestValidateID(unittest.TestCase):

    def test_valid_author_id(self):
        self.assertTrue(
            validate_id("author", "AUT20260001")
        )

    def test_valid_publisher_id(self):
        self.assertTrue(
            validate_id("publisher", "PUB20260001")
        )

    def test_valid_member_id(self):
        self.assertTrue(
            validate_id("member", "MEM20260001")
        )

    def test_valid_book_id(self):
        self.assertTrue(
            validate_id("book", "BOOK20260001")
        )

    def test_valid_borrowing_id(self):
        self.assertTrue(
            validate_id("borrowing", "BOR20260001")
        )

    def test_wrong_prefix(self):
        self.assertFalse(
            validate_id("book", "AUT20260001")
        )

    def test_wrong_length(self):
        self.assertFalse(
            validate_id("book", "BOOK20261")
        )

    def test_unknown_object_type(self):
        self.assertFalse(
            validate_id("banana", "BAN20260001")
        )


class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(
            validate_email("alice@example.com")
        )

    def test_invalid_email_without_at(self):
        self.assertFalse(
            validate_email("aliceexample.com")
        )

    def test_invalid_email_without_domain(self):
        self.assertFalse(
            validate_email("alice@")
        )


class TestValidateName(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(
            validate_name("George Orwell")
        )

    def test_empty_name(self):
        self.assertFalse(
            validate_name("")
        )

    def test_whitespace_name(self):
        self.assertFalse(
            validate_name("   ")
        )

    def test_name_over_100_characters(self):
        self.assertFalse(
            validate_name("A" * 101)
        )


class TestValidateTitle(unittest.TestCase):

    def test_valid_title(self):
        self.assertTrue(
            validate_title("The Hobbit")
        )

    def test_empty_title(self):
        self.assertFalse(
            validate_title("")
        )

    def test_title_over_200_characters(self):
        self.assertFalse(
            validate_title("A" * 201)
        )


class TestValidateAuthor(unittest.TestCase):

    def test_valid_author(self):
        author = Author(
            "AUT20260001",
            "George Orwell"
        )

        self.assertTrue(
            validate_author(author)
        )

    def test_invalid_author_type(self):
        self.assertFalse(
            validate_author("George Orwell")
        )

    def test_invalid_author_id(self):
        author = Author(
            "WRONG",
            "George Orwell"
        )

        self.assertFalse(
            validate_author(author)
        )


class TestValidateCategory(unittest.TestCase):

    def test_valid_category(self):
        self.assertTrue(
            validate_category(Category.FICTION)
        )

    def test_invalid_category(self):
        self.assertFalse(
            validate_category("Fiction")
        )


class TestValidatePublishedDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(
            validate_published_date("2026-09-25")
        )

    def test_invalid_date(self):
        self.assertFalse(
            validate_published_date("2026-99-99")
        )

    def test_wrong_format(self):
        self.assertFalse(
            validate_published_date("25-09-2026")
        )


class TestValidatePublisher(unittest.TestCase):

    def test_valid_publisher(self):
        publisher = Publisher(
            "PUB20260001",
            "Penguin Books",
            "London"
        )

        self.assertTrue(
            validate_publisher(publisher)
        )

    def test_invalid_publisher(self):
        self.assertFalse(
            validate_publisher("Penguin Books")
        )


class TestValidateCity(unittest.TestCase):

    def test_valid_city(self):
        self.assertTrue(
            validate_city("London")
        )

    def test_empty_city(self):
        self.assertFalse(
            validate_city("")
        )

    def test_city_over_100_characters(self):
        self.assertFalse(
            validate_city("A" * 101)
        )


class TestValidateBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(
            book_id="BOOK20260001",
            title="1984",
            authors=[],
            publisher=None,
            categories=[],
            available=True,
            published_date=date(1949, 6, 8)
        )

    def test_valid_book(self):
        self.assertTrue(
            validate_book(self.book)
        )

    def test_invalid_book_type(self):
        self.assertFalse(
            validate_book("1984")
        )

    def test_invalid_book_id(self):
        self.book.book_id = "WRONG"

        self.assertFalse(
            validate_book(self.book)
        )

    def test_invalid_title(self):
        self.book.title = ""

        self.assertFalse(
            validate_book(self.book)
        )


class TestGetID(unittest.TestCase):

    @patch("builtins.input", return_value="0001")
    def test_get_book_id(self, mock_input):
        result = get_id("book")

        self.assertEqual(
            result,
            "BOOK20260001"
        )

    @patch("builtins.input", return_value="")
    def test_optional_id_returns_none(self, mock_input):
        result = get_id(
            "book",
            required=False
        )

        self.assertIsNone(result)


class TestGetName(unittest.TestCase):

    @patch("builtins.input", return_value="George Orwell")
    def test_get_name(self, mock_input):
        result = get_name("author")

        self.assertEqual(
            result,
            "George Orwell"
        )


class TestGetEmail(unittest.TestCase):

    @patch("builtins.input", return_value="alice@example.com")
    def test_get_email(self, mock_input):
        result = get_email()

        self.assertEqual(
            result,
            "alice@example.com"
        )


class TestGetTitle(unittest.TestCase):

    @patch("builtins.input", return_value="1984")
    def test_get_title(self, mock_input):
        result = get_title()

        self.assertEqual(
            result,
            "1984"
        )


class TestGetCity(unittest.TestCase):

    @patch("builtins.input", return_value="london")
    def test_get_city_title_cases_input(self, mock_input):
        result = get_city()

        self.assertEqual(
            result,
            "London"
        )


class TestGetPublishedDate(unittest.TestCase):

    @patch("builtins.input", return_value="1949-06-08")
    def test_get_published_date(self, mock_input):
        result = get_published_date()

        self.assertEqual(
            result,
            date(1949, 6, 8)
        )


if __name__ == "__main__":
    unittest.main()