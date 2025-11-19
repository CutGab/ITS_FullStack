# --------------------------
# Book Class
# --------------------------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return self.title + " by " + self.author + " (ISBN: " + self.isbn + ")"

    @classmethod
    def from_string(cls, book_str):
        # Split string by comma manually
        details = book_str.split(",")
        # Remove spaces from each part
        title = details[0].strip()
        author = details[1].strip()
        isbn = details[2].strip()
        return cls(title, author, isbn)


# --------------------------
# Member Class
# --------------------------
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = int(member_id)
        self.borrowed_books = []  # List to keep track of borrowed books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        if len(self.borrowed_books) == 0:
            borrowed_str = "None"
        else:
            borrowed_str = ""
            for book in self.borrowed_books:
                borrowed_str = borrowed_str + book.title + ", "
            borrowed_str = borrowed_str[:-2]  # remove last comma and space
        return self.name + " (ID: " + str(self.member_id) + ") - Borrowed Books: " + borrowed_str

    @classmethod
    def from_string(cls, member_str):
        details = member_str.split(",")
        name = details[0].strip()
        member_id = details[1].strip()
        return cls(name, member_id)


# --------------------------
# Library Class
# --------------------------
class Library:
    total_books = 0  # Class attribute

    def __init__(self):
        self.books = []    # List of available books
        self.members = []  # List of registered members

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            Library.total_books -= 1

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book not in self.books:
            return "Sorry, '" + book.title + "' is not available."
        if member not in self.members:
            return "Sorry, " + member.name + " is not registered."
        member.borrow_book(book)
        self.remove_book(book)
        return "'" + book.title + "' has been lent to " + member.name + "."

    def __str__(self):
        books_list = ""
        for book in self.books:
            books_list = books_list + book.title + ", "
        if books_list != "":
            books_list = books_list[:-2]

        members_list = ""
        for member in self.members:
            members_list = members_list + member.name + ", "
        if members_list != "":
            members_list = members_list[:-2]

        return "Library Books: " + books_list + "\nLibrary Members: " + members_list + "\nTotal Books: " + str(Library.total_books)

    @classmethod
    def library_statistics(cls):
        print("Total books in all libraries: " + str(cls.total_books))


# --------------------------
# DRIVER PROGRAM
# --------------------------

# Create books
b1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
b2 = Book.from_string("Barzellette Totti, Totti, 1234567809")

# Create members
m1 = Member.from_string("Mario Rossi, 1")
m2 = Member.from_string("Luigi Verdi, 2")

# Create library
library = Library()

# Add books to library
library.add_book(b1)
library.add_book(b2)

# Register members
library.register_member(m1)
library.register_member(m2)

# Print library before lending
print("Before lending books:")
print(library)
print()

# Lend books
print(library.lend_book(b1, m1))
print(library.lend_book(b2, m2))
print()

# Print library after lending
print("After lending books:")
print(library)
print()

# Show member borrowed books
print("Member details:")
print(m1)
print(m2)
print()

# Show total books
Library.library_statistics()
