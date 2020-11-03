class Library(object):
    def __init__(self):
        self.books = {}

    def __del__(self):
        self.books = {}

    def get_quantity(self, book):
        print(self.books[book], end=' ')

    def get_book(self, book):
        self.books[book] -= 1
        print(self.books[book], end=' ')

    def return_book(self, book):
        self.books[book] += 1
        print(self.books[book], end=' ')


a = Library()
books_init = input().split()

for i in range(0, len(books_init), 2):
    a.books[books_init[i]] = int(books_init[i + 1])

for book in a.books:
    print(book, end=' ')
    a.get_quantity(book)
    a.get_book(book)
    a.return_book(book)
