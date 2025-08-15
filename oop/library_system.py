class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size = 0):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size}kB"

class PrintBook(Book):
    def __init__(self, title, author, page_count = 0):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"PrintBook: {super().__str__()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"{book}")
        else:
            print("Only instances of Book can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)