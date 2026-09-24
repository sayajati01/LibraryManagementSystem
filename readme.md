# Library Management System

A command-line Library Management System built with Python and SQLite.

The project is designed around a layered structure separating data models, database operations, application services, input validation, and the CLI interface.

## Current Status

The system is currently under development.

Implemented functionality includes:

- Publisher management
- Author management
- Member management
- Book creation and viewing
- Book updating
- Book-author relationships
- Book-category relationships
- Category initialization
- SQLite database connection and table creation
- Input validation
- Entity ID generation and validation

Additional features will be documented here as they are implemented.

## Technologies

- **Python**
- **SQLite**
- Python standard library:
  - `sqlite3`
  - `dataclasses`
  - `enum`
  - `datetime`
  - `pathlib`
  - `re`

No external Python packages are currently required.

## Project Structure

```text
.
├── main.py
├── models.py
├── services.py
├── storage.py
├── utils.py
└── library.db
```

### `main.py`

The CLI entry point of the application.

Responsible for:

- Starting the application
- Creating the database connection
- Initializing database tables
- Initializing predefined book categories
- Displaying the main menu
- Routing menu selections to the appropriate feature

The main menu currently provides access to:

```text
1. Book Management
2. Member Management
3. Borrowing Management
4. Search Books
5. Publisher Management
6. Author Management
7. Library Statistics
0. Exit
```

Some menu options are still under development.

### `models.py`

Contains the application's data models.

#### Publisher

```python
Publisher(
    publisher_id,
    publisher_name,
    publisher_city
)
```

Represents a book publisher.

#### Author

```python
Author(
    author_id,
    author_name
)
```

Represents a book author.

#### Member

```python
Member(
    member_id,
    member_name,
    member_email,
    member_status
)
```

Represents a library member.

Members can have one of two statuses:

```text
Active
Inactive
```

#### Book

```python
Book(
    book_id,
    title,
    authors,
    publisher,
    categories,
    available,
    published_date
)
```

Represents a library book.

A book can have:

- Multiple authors
- Multiple categories
- One publisher or no publisher
- An availability status
- A publication date

The `Book` class also provides:

```python
is_available()
```

to return its current availability status.

#### Borrowing

```python
Borrowing(
    borrowing_id,
    member_id,
    book_id,
    borrow_date,
    return_date
)
```

Represents the relationship between a member and a borrowed book.

The borrowing model is defined, while the borrowing operations are still under development.

#### Category

Book categories are represented using an `Enum`.

Current categories include:

- Fiction
- Non-Fiction
- Mystery
- Thriller
- Horror
- Romance
- Fantasy
- Science Fiction
- Historical
- Biography
- Autobiography
- Self-Help
- Philosophy
- Psychology
- Science
- Technology
- Business
- History
- Poetry
- Drama
- Children
- Education
- Travel
- Cooking
- Religion
- Other

## Database

The application uses SQLite for persistent storage.

The database file is:

```text
library.db
```

The connection enables SQLite foreign-key enforcement:

```sql
PRAGMA foreign_keys = ON
```

The database design contains tables for:

- Publishers
- Authors
- Members
- Books
- Categories
- Book-author relationships
- Book-category relationships
- Borrowings

### Relationships

A book can have multiple authors:

```text
Book ───< BookAuthor >─── Author
```

A book can belong to multiple categories:

```text
Book ───< BookCategory >─── Category
```

A book can optionally reference one publisher:

```text
Publisher ───< Book
```

A borrowing connects a member with a book:

```text
Member ───< Borrowing >─── Book
```

## Implemented Features

### Publisher Management

Currently implemented:

- Add publisher
- Update publisher
- Delete publisher
- View a publisher
- View all publishers
- Check whether a publisher exists
- Retrieve a publisher from the database

A publisher contains:

```text
Publisher ID
Publisher Name
Publisher City
```

### Author Management

Currently implemented:

- Add author
- Update author
- Delete author
- View an author
- View all authors
- Check whether an author exists
- Retrieve an author from the database

An author contains:

```text
Author ID
Author Name
```

### Member Management

Currently implemented:

- Add member
- Update member
- Delete member
- Activate member
- Deactivate member
- View a member
- View all members
- Check whether a member exists
- Retrieve a member from the database

A member contains:

```text
Member ID
Member Name
Member Email
Member Status
```

New members are initially created as:

```text
Active
```

### Book Management

Currently implemented:

- Add a book
- Update a book
- View a book
- View all books
- Retrieve a book from the database
- Check whether a book exists
- Store book-author relationships
- Store book-category relationships

When adding a book, the application collects:

```text
Book ID
Title
Authors
Publisher
Categories
Availability
Published Date
```

New books are initially marked as available.

The book update interface currently supports updating:

```text
Title
Authors
Publisher
Categories
Published Date
```

### Category Management

Categories are predefined through the `Category` enum.

On application startup, the predefined categories are inserted into the database if they do not already exist.

Category IDs use the format:

```text
CAT0001
CAT0002
CAT0003
...
```

## Input Validation

`utils.py` contains reusable input and validation functions.

### ID Validation

Entity IDs follow predefined prefixes:

| Entity | Prefix | Example |
|---|---|---|
| Author | `AUT` | `AUT20260001` |
| Publisher | `PUB` | `PUB20260001` |
| Member | `MEM` | `MEM20260001` |
| Book | `BOOK` | `BOOK20260001` |
| Borrowing | `BOR` | `BOR20260001` |
| Category | `CAT` | `CAT0001` |

IDs for authors, publishers, members, books, and borrowings contain an eight-digit numeric section after the entity prefix.

### Email Validation

Member email addresses are validated using a regular expression.

### Name Validation

Names must:

- Not be empty
- Be no longer than 100 characters

### Book Title Validation

Book titles must:

- Not be empty
- Be no longer than 200 characters

### Publication Date Validation

Publication dates must follow:

```text
YYYY-MM-DD
```

and must represent a valid date.

### City Validation

Cities must:

- Not be empty
- Be no longer than 100 characters

### Entity Validation

The project also contains validation functions for:

- Authors
- Publishers
- Categories
- Books

## Application Architecture

The project separates responsibilities into several layers.

```text
                 ┌──────────────┐
                 │   main.py    │
                 │  CLI / Menu  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ services.py  │
                 │ Application  │
                 │   Logic      │
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      ┌──────────────┐      ┌──────────────┐
      │   utils.py   │      │  storage.py  │
      │ Validation & │      │ SQLite / DB  │
      │    Input     │      │ Operations   │
      └──────────────┘      └──────┬───────┘
                                   │
                                   ▼
                            ┌──────────────┐
                            │  library.db  │
                            └──────────────┘

                 models.py
                     ▲
                     │
             Data Model Definitions
```

### Responsibility of Each Layer

**`main.py`**

Handles the CLI and menu navigation.

**`services.py`**

Contains application-level operations such as adding, updating, deleting, and displaying entities.

**`storage.py`**

Handles SQLite operations and reconstruction of Python model objects from database records.

**`utils.py`**

Handles user input and reusable validation logic.

**`models.py`**

Defines the application's data structures.

## Running the Application

Make sure Python is installed, then run:

```bash
python main.py
```

On startup, the application:

1. Creates a SQLite connection.
2. Enables foreign-key enforcement.
3. Initializes the database tables.
4. Initializes the predefined categories.
5. Displays the main menu.

The SQLite database is stored locally as:

```text
library.db
```

## Development Notes

This project is being developed incrementally.

The README intentionally documents only functionality that is currently implemented. Features represented by menu entries but whose underlying implementation has not yet been completed are not described as functional.

As new functionality is implemented, its behavior, usage, and relevant database relationships can be added to this README.

## License

No license has been specified yet.