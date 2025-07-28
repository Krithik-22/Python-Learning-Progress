class Book:
    #Dunder methods
    def __init__(self, title, author):
        self.title = title
        self.author = author

    #When len() is used on object, this is the method called we can customize len() for our class instances
    def __len__(self):
        return len(self.title)
    
    #when print() is called on our class instance, this is the method it calls, it check for __str__. If __str__ not found it looks for __repr__ in the class. it goes for default __repr__ that will be in the object class
    def __str__(self):
        return f"📘 {self.title} by {self.author}"
    
    #repr() is used for developer friendly messages to print to debug for the object
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
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

# @static and @class methods(Can go to notes for detailed explanation)
class Validator:
    validated = 0

    @staticmethod
    def is_valid_email(email):
        Validator.validated += 1
        if '@' in email and email.endswith('.com'):
            return True
        return False
    
    @classmethod
    def show_total(cls):
        print(f"{cls.validated} emails were validated using this class")


#encapsulation challenge
class SecureNote:
    def __init__(self, content):
        self.__content = content
    
    def get_content(self):
        return self.__content
    
    def set_content(self,new_content):
        self.__content = new_content

note = SecureNote('Hellooooo')
print(note.get_content())
note.set_content('heyyyy')
print(note.get_content())
print(note.__content)#This gives an attribute error

'''email = 'abc@gmail.com123'
Validator.is_valid_email(email)
Validator.show_total()
email1='bca@gmail.com'
Validator.is_valid_email(email1)
Validator.show_total()'''

'''bookshelf = []

talk_to_anyone = Book("how to Talk to Anyone", "Krithik")
atomic_habits_ebook = EBook("Atomic Habits","Krithik",5)
ikigai_audio = AudioBook("ikigai","KSP",47)

bookshelf.append(talk_to_anyone)
bookshelf.append(atomic_habits_ebook)
bookshelf.append(ikigai_audio)

for book in bookshelf:
    book.describe()'''

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

'''🧠 Challenge:
Create a class called Validator with two methods:
@staticmethod is_valid_email(email)
returns True if '@' in email and ends with .com
@classmethod show_total(cls)
Print how many emails were validated using this class
'''

'''Challenge:
Create a class BankAccount with:

Private attribute __balance

deposit(amount)

withdraw(amount)

get_balance()
Make sure withdrawal can’t happen if balance is low.'''

class BankAccount:
    def __init__(self, amount=0):
        self.__amount = amount
    
    def deposit(self, add_amount):
        self.__amount +=add_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__amount:
            print(f"You do not have that much in your account. Remaining Balance: {self.__amount}")
        else:
            self.__amount -= withdraw_amount
    
    def get_balance(self):
        print(f"Balance: {self.__amount}")

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def describe(self):
        print(f"I'm {self.name} and I'm a {self.role}")
    
class Developer(Employee):
    def __init__(self,name,role):
        self.super(name,role)
    def describe(self):
        print(f"I'm {self.name} and I'm a {self.role} - Writes code")

class Manager(Employee):
    def __init__(self,name,role):
        self.super(name,role)
    def describe(self):
        print(f"I'm {self.name} and I'm a {self.role} - manages team")