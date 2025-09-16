from library import Library
from book import Book

library_1 = Library()

print('Welcome to our Library')
print('''What do you wanna do?\n
            1. Add a Book to the Library\n
            2. Add a member to the Library\n
            3. Remove a book from the Library\n
            4. Remove member from the library\n
            5. Borrow a book from the Library\n
            6. return a book to the Library\n
            7. Display all the books in the Library\n
            8. Display all the available books in the Library\n
            9. Display all the members in the Library\n
            10. Display the Books borrowed by me currently\n
            11. Exit\n''')
while True:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        name = input('What is the Title of the book: ')
        author = input('Who is the author: ')
        book = Book(name,author)
        library_1.add_book(book)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        library_1.display_books()
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    else:
        break