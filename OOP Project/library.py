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

    @classmethod
    def return_book_id(self, book_name):
        for id, book in self._books.items():
            if book_name == book:
                return id
        return None

    def borrow_book(self, book, member_id):
        book_id = Library.return_book_id(book)
        if book_id == None:
            print('Book not found in our Library')
            return None
        book = self._books[book_id]
        book.borrow(member_id)
        self._members[member_id].add_book_to_my_list(book)

    def return_book(self, book, member_id):
        book_id = Library.return_book_id(book)
        book = self._books[book_id]
        book.return_book()
        self._members[member_id].remove_book_from_my_list(book)

    def display_available_books(self):
        for id,book in self._books.items():
            if book.is_available:
                print(f'{id}:{book}')
    
    def books_borrowed_by_member(self, member_id):
        member = self._members[member_id]
        borrowed_books = member.borrowed_books
        for book in borrowed_books:
            print(book)
