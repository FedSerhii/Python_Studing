class Book:
    def __init__(self, title, author, year, page_count):
        self.title = title
        self.author = author
        self.year = year
        self.page_count = page_count

    @staticmethod
    def count_book_by_years(books, year):
        count = 0
        for book in books:
            if book.year == year:
                count += 1
        return count

book1 = Book('The Little Prince', 'Antoine de Saint-Exupéry', 1943, 1450)
book2 = Book('The Name of the Rose', 'Umberto Eco', 1980, 987)
book3 = Book('Lord Jim', 'Joseph Conrad', 1900, 657)

books = [book1, book2, book3]

year = 1980
count = Book.count_book_by_years(books, year)
print(f'In {year} was publish {count} book')