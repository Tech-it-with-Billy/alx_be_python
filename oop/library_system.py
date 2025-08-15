class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size = 0):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count = 0):
        super().__init__(title, author)
        self.pages = page_count

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        elif isinstance(book, EBook):
            self.books.append(book)
        elif isinstance(book, PrintBook):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")
    
    def list_books(self):
        return [str(book) for book in self.books]