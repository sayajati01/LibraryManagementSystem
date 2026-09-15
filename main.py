from services import *
from storage import create_connection,create_tables


# =========================
# STATISTICS
# =========================
def statistic_menu():
    print("""
-------- STATISTICS MENU --------
1. Total Books
2. Total Members
3. Total Publishers
4. Total Authors
5. Currently Borrowed Books
6. Available Books
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        show_total_books()
    elif menu_choice == "2":
        show_total_members()
    elif menu_choice == "3":
        show_total_publishers()
    elif menu_choice == "4":
        show_total_authors()
    elif menu_choice == "5":
        show_currently_borrowed_books()
    elif menu_choice == "6":
        show_available_books()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# AUTHOR MANAGEMENT
# =========================
def author_management_menu():
    print("""
-------- AUTHOR MANAGEMENT MENU --------
1. Add Author
2. Update Author
3. Delete Author
4. View Author
5. View All Authors
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        add_author()
    elif menu_choice == "2":
        update_author()
    elif menu_choice == "3":
        delete_author()
    elif menu_choice == "4":
        view_author()
    elif menu_choice == "5":
        view_all_authors()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# PUBLISHER MANAGEMENT
# =========================
def publisher_management_menu():
    print("""
-------- PUBLISHER MANAGEMENT MENU --------
1. Add Publisher
2. Update Publisher
3. Delete Publisher
4. View Publisher
5. View All Publishers
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        add_publisher()
    elif menu_choice == "2":
        update_publisher()
    elif menu_choice == "3":
        delete_publisher()
    elif menu_choice == "4":
        view_publisher()
    elif menu_choice == "5":
        view_all_publishers()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# SEARCH
# =========================
def search_menu():
    print("""
-------- SEARCH MENU --------
1. Search by Book ID
2. Search by Title
3. Search by Author
4. Search by Category
5. Search by Publisher
6. Search by Publication Year
7. Advanced Search
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        search_by_book_id()
    elif menu_choice == "2":
        search_by_title()
    elif menu_choice == "3":
        search_by_author()
    elif menu_choice == "4":
        search_by_category()
    elif menu_choice == "5":
        search_by_publisher()
    elif menu_choice == "6":
        search_by_publication_year()
    elif menu_choice == "7":
        advanced_search()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# BORROWING
# =========================
def borrowing_feature_menu():
    print("""
-------- BORROWING FEATURE MENU --------
1. Borrow Book
2. Return Book
3. View Member's Borrowed Books
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        borrow_book()
    elif menu_choice == "2":
        return_book()
    elif menu_choice == "3":
        get_member_borrowed_books()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# MEMBER MANAGEMENT
# =========================
def member_management_menu():
    print("""
-------- MEMBER MANAGEMENT MENU --------
1. Add Member
2. Update Member
3. Delete Member
4. View Member
5. View All Members
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        add_member()
    elif menu_choice == "2":
        update_member()
    elif menu_choice == "3":
        delete_member()
    elif menu_choice == "4":
        view_member()
    elif menu_choice == "5":
        view_all_members()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# BOOK MANAGEMENT
# =========================
def book_management_menu():
    print("""
-------- BOOK MANAGEMENT MENU --------
1. Add Book
2. Update Book
3. Delete Book
4. View All Books
5. View Book
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        add_book()
    elif menu_choice == "2":
        update_book()
    elif menu_choice == "3":
        delete_book()
    elif menu_choice == "4":
        view_all_books()
    elif menu_choice == "5":
        view_book()
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# MAIN MENU
# =========================

def display_menu():
    print("""
===== LIBRARY MANAGEMENT SYSTEM =====
1. Book Management
2. Member Management
3. Borrowing Management
4. Search Books
5. Publisher Management
6. Author Management
7. Library Statistics
0. Exit
""")


def main():
    running = True
    connection = create_connection()
    create_tables(connection)

    while running:
        display_menu()

        menu_choice = input("Input Menu (number): ").strip()

        if menu_choice == "1":
            book_management_menu()
        elif menu_choice == "2":
            member_management_menu()
        elif menu_choice == "3":
            borrowing_feature_menu()
        elif menu_choice == "4":
            search_menu()
        elif menu_choice == "5":
            publisher_management_menu()
        elif menu_choice == "6":
            author_management_menu()
        elif menu_choice == "7":
            statistic_menu()
        elif menu_choice == "0":
            running = False
        else:
            print("INVALID MENU")


if __name__ == "__main__":
    main()