class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        if self.books:
            info = '\n'.join(str(book) for book in self.books)
            return f'At the moment, the library has such books:\n{info}'
        else:
            return 'Library is empty!'


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} - {self.author} in {self.year}'


library = Library()

book1 = Book('The Little Prince', 'Antoine de Saint-Exupéry', 1943)
book2 = Book('The Name of the Rose', 'Umberto Eco', 1980)
book3 = Book('Lord Jim', 'Joseph Conrad', 1900)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)