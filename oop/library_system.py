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
            print(f"Book added: {book}")
        else:
            print("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\nLibrary Collection:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")