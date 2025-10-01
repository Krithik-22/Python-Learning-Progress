from book import Book

class Library:
    _members = {}
    _books = {}

    def __init__(self):
        pass

    def add_book(self, book):
        id = int(max(self._books.keys(), default = 0)) + 1
        self._books[id] = book
        print(f'Book with id:{id} has been added succesfully to the Library')

    def display_books(self):
        for id,book in self._books.items():
            print(f'{id}:{book}')

    def remove_book(self,id):
        del self._books[id]

    def add_member(self, member):
        id = int(max(self._members.keys(), default = 0)) + 1
        self._members[id] = member
        print(f'member with id:{id} has been added succesfully to the Library')

    def remove_member(self, id):
        del self._members[id]

    def display_members(self):
        for id, member in self._members.items():
            print(f'{id}: {member}')


    def borrow_book(self, book_id, member_id):
        book = self._books[book_id]
        book.borrow(member_id)
