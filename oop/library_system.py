class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size = 0):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{self.title} by {self.author}, file size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count = 0):
        super().__init__(title, author)
        self.pages = page_count
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

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