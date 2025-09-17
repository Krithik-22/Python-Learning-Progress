class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_available = True
        self.due_date = ''
        self.borrowed_by = ''
    
    def __str__(self):
        return f'{self.name} by {self.author}'

    def borrow(self, member_id):
        if self.is_available:
            self.is_available = False
            self.borrowed_by = member_id
            self.due_date = 'now'
            print(f'Book is borrowed by Member: {member_id}')
        print(f'Sorry! Book is currently unavailable. You may come back on {self.due_date}')

    def return_book(self):
        self.is_available = True
        self.borrowed_by = ''

