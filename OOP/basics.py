class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def describe(self):
        print(f"Book: {self.title} by {self.author}")
    def is_long_title(self):
        return len(self.title) > 15


#Inheritance syntax and all
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title,author) #calls parent constructor
        self.file_size = file_size
    
    #This overrides the parent classes method and when an object created using this child class calls describe(), it uses this method
    def describe(self):
        print(f"EBook: {self.title} by {self.author} - {self.file_size} MB")


class AudioBook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title,author)
        self.duration = duration
    def describe(self):
        print(f"Audio Book: {self.title} by {self.author} - {self.duration} Min(s)")

bookshelf = []

talk_to_anyone = Book("how to Talk to Anyone", "Krithik")
atomic_habits_ebook = EBook("Atomic Habits","Krithik",5)
ikigai_audio = AudioBook("ikigai","KSP",47)

bookshelf.append(talk_to_anyone)
bookshelf.append(atomic_habits_ebook)
bookshelf.append(ikigai_audio)

for book in bookshelf:
    book.describe()

'''n = int(input('Enter the number of books you want to create: '))

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
    book.describe()'''