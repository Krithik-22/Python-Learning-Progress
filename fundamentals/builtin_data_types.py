#Dictionary
#Challenege 1 - Contact List book
'''phonebook = {}

while True:
    name = input("Enter your name to add to the list:")
    number = input("Enter your number to add to the list:")
    if len(number) == 10 and number.isdigit():
        phonebook[name] = number
    elif name in phonebook:
        toUpdate = input(f"{name} already exists in phonebook. Do you want to update the number?\n")
        if toUpdate == 'yes':
            number = input(f"Enter updated number of {name}:")
            if len(number) == 10 and number.isdigit():
                phonebook[name] = number
            else:
                print("Enter a valid phone number to add to list")
                continue
        else: 
            continue
    else:
        print("Enter a valid phone number to add to list")
        continue
    toBreak = input("Want to add another contact? ")
    if toBreak == 'no':
        break;

for name,num in phonebook.items():
    print(f"{name}'s number: {num}")'''


#Sets
#Challenege 1 - Print all unique words from the string
text = "apple banana apple mango banana orange"

'''text = text.split()
unique = set()
'''

'''unique = set(text.split())

for item in unique:
    print(f"{item}")
'''

'''🧠 Challenge #2: Count Unique Words
Problem:
Given a sentence from the user, extract the unique words and also count how many times each word appears.
'''
'''
text = input("Enter a sentence:")

text = text.split()
count = {}

for item in text:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print(count)
for key,value in count.items():
    if count[key] == 1:
        print(f"{key}")'''

unique = set()

for word in text:
    if word in unique:
        unique.remove(word)
    else:
        unique.add(word)

#print(unique)



#List comprehension
nums = [1, 2, 3, 4, 5]
squares = [n*n for n in nums]
even_squares = [n*n for n in nums if n%2==0]
#print(even_squares)


#nested list comprehension
#Challenge convert this to 2D list to a 1D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''wrong way to do it
matrix_1d = [n for n in (num for num in matrix)]'''

matrix_1d = [n for row in matrix for n in row]
#print(matrix_1d)

#dictionary comprehension
#dictionary of numbers and their squares
sq_nums = {n:n**2 for n in range(1,6)}
#print(sq_nums)

#dictionary of even num and their sq
even_sq_nums = {n:n**2 for n in range(10) if n%2==0}
#print(even_sq_nums)

#invert a dictionary
dict = {'a':1,'b':2,'c':3}
invert = {v:k for k,v in dict.items()}
#print(invert)


#Challenge 1
#Create a dictionary from the list of numbers below, where the key is the number and the value is "even" or "odd" depending on whether the number is even or odd

nums = [1, 2, 3, 4, 5, 6]
odd_even_dict = {n:'even' if n%2==0 else 'odd' for n in nums}

print(odd_even_dict)


#Given a list of names, create a dictionary with the names as keys and their lengths as values.
names = ["Krithik", "Sai", "Dhoni", "Kohli"]

name_len = {name:len(name) for name in names}

print(name_len)

#You are given a nested list of strings, and you need to count how many times each word appears, and return it as a dictionary

sentences = [
    ["python", "is", "fun"],
    ["lambda", "functions", "are", "cool"],
    ["python", "is", "powerful"]
]

words = [word for row in sentences for word in row]

dict_count = {word:words.count(word) for word in words}

print(dict_count)