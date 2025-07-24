class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def describe(self):
        print(f"Book: {self.title} by {self.author}")
    def is_long_title(self):
        return len(self.title) > 15

bookshelf = []

n = int(input('Enter the number of books you want to create: '))

for i in range(n):
    title = input('Enter the title of your book: ')
    author = input('Who is the author: ')
    bookshelf.append(Book(title,author))


print("These are all the books added!!")
for book in bookshelf:
    book.describe();

long_books = [book for book in bookshelf if book.is_long_title()]

print("These are all the long books in the shelf!!")
for book in long_books:
    book.describe()