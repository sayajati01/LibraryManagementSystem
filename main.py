from services import *
from storage import create_connection,create_tables,insert_category_into_db


# =========================
# PUBLISHER MANAGEMENT
# =========================
def publisher_management_menu(connection):
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
        add_publisher(connection)
    elif menu_choice == "2":
        update_publisher(connection)
    elif menu_choice == "3":
        delete_publisher(connection)
    elif menu_choice == "4":
        view_publisher(connection)
    elif menu_choice == "5":
        view_all_publishers(connection)
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")

# =========================
# AUTHOR MANAGEMENT
# =========================
def author_management_menu(connection):
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
        add_author(connection)
    elif menu_choice == "2":
        update_author(connection)
    elif menu_choice == "3":
        delete_author(connection)
    elif menu_choice == "4":
        view_author(connection)
    elif menu_choice == "5":
        view_all_authors(connection)
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# MEMBER MANAGEMENT
# =========================
def member_management_menu(connection):
    print("""
-------- MEMBER MANAGEMENT MENU --------
1. Add Member
2. Update Member
3. Delete Member
4. Activate Member
5. Deactivate Member
6. View Member
7. View All Members
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        add_member(connection)
    elif menu_choice == "2":
        update_member(connection)
    elif menu_choice == "3":
        delete_member(connection)
    elif menu_choice == "4":
        activate_member(connection)
    elif menu_choice == "5":
        deactivate_member(connection)
    elif menu_choice == "6":
        view_member(connection)
    elif menu_choice == "7":
        view_all_members(connection)
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# BORROWING
# =========================
def borrowing_feature_menu(connection):
    print("""
-------- BORROWING FEATURE MENU --------
1. Borrow Book
2. Return Book
3. View Member's Borrowed Books
0. Back
""")

    menu_choice = input("Input Menu (number): ").strip()

    if menu_choice == "1":
        borrow_book(connection)
    elif menu_choice == "2":
        return_book(connection)
    elif menu_choice == "3":
        display_member_borrowed_books(connection)
    elif menu_choice == "0":
        return
    else:
        print("INVALID MENU")


# =========================
# BOOK MANAGEMENT
# =========================
def book_management_menu(connection):
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
        add_book(connection)
    elif menu_choice == "2":
        update_book(connection)
    elif menu_choice == "3":
        delete_book(connection)
    elif menu_choice == "4":
        view_all_books(connection)
    elif menu_choice == "5":
        view_book(connection)
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
    insert_category_into_db(connection)

    while running:
        display_menu()

        menu_choice = input("Input Menu (number): ").strip()

        if menu_choice == "1":
            book_management_menu(connection)
        elif menu_choice == "2":
            member_management_menu(connection)
        elif menu_choice == "3":
            borrowing_feature_menu(connection)
        elif menu_choice == "4":
            print("Currently Unavailable.\n")
        elif menu_choice == "5":
            publisher_management_menu(connection)
        elif menu_choice == "6":
            author_management_menu(connection)
        elif menu_choice == "7":
            display_statistics(connection)
        elif menu_choice == "0":
            running = False
        else:
            print("INVALID MENU")


if __name__ == "__main__":
    main()