from datetime import datetime, timedelta
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_available = True
        self.due_date = ''
        self.borrowed_by = ''
    
    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def __eq__(self, value):
        return value in self.name

    def borrow(self, member_id):
        if self.is_available:
            self.is_available = False
            self.borrowed_by = member_id
            self.due_date = datetime.now() + timedelta(10)
            print(f'Book is borrowed by Member: {member_id} and the due date is to return it on/before {self.due_date}')
        else:
            print(f'Sorry! Book is currently unavailable. You may come back on {self.due_date}')

    def return_book(self):
        if self.due_date > datetime.now():
            print('Book has been returned befor the due date')
            self.due_date = ''
            self.is_available = True
            self.borrowed_by = ''
        else:
            print('You have crossed the due dat. Kindly pay a fine and return the book')

