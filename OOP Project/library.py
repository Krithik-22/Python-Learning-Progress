from book import Book

class Library:
    _members = {}
    _books = {}

    def __init__(self):
        pass

    def add_book(self, book):
        id = int(max([book in self._books.keys()], default = 0)) + 1
        self._books[id] = book

    def display_books(self):
        for book in self._books.values():
            print(book)

    def remove_book(self,id):
        del self._books[id]

    def add_member(self, member):
        id = int(max([member in self._members.keys()], default = 0)) + 1
        self._members[id] = member

    def remove_member(self, id):
        del self._members[id]

    def borrow_book(self, book_id, member_id):
        book = self._books[book_id]
        book.borrow(member_id)


    