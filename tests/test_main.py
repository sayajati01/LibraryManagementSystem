import unittest
from unittest.mock import patch

import main


class TestBookManagementMenu(unittest.TestCase):

    @patch("main.view_all_books")
    @patch("builtins.input", return_value="4")
    def test_view_all_books_menu(
        self,
        mock_input,
        mock_view
    ):
        main.book_management_menu("connection")

        mock_view.assert_called_once_with(
            "connection"
        )


class TestBorrowingMenu(unittest.TestCase):

    @patch("main.borrow_book")
    @patch("builtins.input", return_value="1")
    def test_borrow_book_menu(
        self,
        mock_input,
        mock_borrow
    ):
        main.borrowing_feature_menu("connection")

        mock_borrow.assert_called_once_with(
            "connection"
        )


class TestAuthorMenu(unittest.TestCase):

    @patch("main.add_author")
    @patch("builtins.input", return_value="1")
    def test_add_author_menu(
        self,
        mock_input,
        mock_add
    ):
        main.author_management_menu("connection")

        mock_add.assert_called_once_with(
            "connection"
        )


class TestPublisherMenu(unittest.TestCase):

    @patch("main.add_publisher")
    @patch("builtins.input", return_value="1")
    def test_add_publisher_menu(
        self,
        mock_input,
        mock_add
    ):
        main.publisher_management_menu("connection")

        mock_add.assert_called_once_with(
            "connection"
        )


class TestMemberMenu(unittest.TestCase):

    @patch("main.add_member")
    @patch("builtins.input", return_value="1")
    def test_add_member_menu(
        self,
        mock_input,
        mock_add
    ):
        main.member_management_menu("connection")

        mock_add.assert_called_once_with(
            "connection"
        )


class TestMainMenu(unittest.TestCase):

    @patch("main.borrowing_feature_menu")
    @patch("main.insert_category_into_db")
    @patch("main.create_tables")
    @patch("main.create_connection")
    @patch("main.input", return_value="0")
    def test_main_exit(
        self,
        mock_input,
        mock_create_connection,
        mock_create_tables,
        mock_insert_category,
        mock_borrowing_menu
    ):
        mock_create_connection.return_value = "connection"

        main.main()

        mock_create_connection.assert_called_once()
        mock_create_tables.assert_called_once_with(
            "connection"
        )
        mock_insert_category.assert_called_once_with(
            "connection"
        )

        mock_borrowing_menu.assert_not_called()