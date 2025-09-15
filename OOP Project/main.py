from library import Library
from books import Book

book1 = Book('ABC','KSP')

library1 = Library()

library1.add_book(book1)

library1.display_books()