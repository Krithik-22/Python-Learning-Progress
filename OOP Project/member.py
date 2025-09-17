class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def __str__(self):
        return f'{self.name}'

    def add_book_to_my_list(self, book):
        self.borrowed_books.append(book)