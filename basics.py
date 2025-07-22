#Learning about data types
name="Krithik"
age = 21
height = 6.3
isCool = True

#print(name, age, height, isCool)

#Mini challenge
'''userName = input("Enter your name: ")
userAge = int(input("Enter your age: "))
#print("Hello ", userName, ", In 5 years you will be ", userAge + 5)
print(f"Hello {userName}! In 5 years you will be {userAge + 5}")
'''
#Learning Operators & Expressions
#Mini Challenge
'''num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"Sum: {num1 + num2}\nDifference: {num1 - num2}\n")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal")
'''
#Learning Conditionals
#Mini Challenge
'''haveVoterId = input("Do you have a Voter ID? ")

if userAge >= 18 and haveVoterId == 'yes':
    print('You are eligible to vote')
elif userAge >= 18 and haveVoterId == 'no':
    print('You are eligible to vote but you need a voter ID')
else:
    print('You cannot vote')
'''
#Learning loops
#Mini Challenge

'''toContinue = True

while toContinue:
    n = input("Enter a number or type 'exit' to quit: ")

    if n == 'exit':
        #toContinue = False
        break;

    if n.isdigit():
        n = int(n)
    
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")'''

#Learning Lists & Strings

'''fruits = ['apple','mango','orange']

for fruit in fruits:
    if fruit == 'apple':
        idx = fruits.index(fruit)
        fruits[idx] = 'pomogranate'
print(fruits)'''

#mini challenege
'''groceryList = ["milk", "eggs", "bread", "butter", "toothpaste"]

groceryList = ['cheese' if item == 'toothpaste' else item for item in groceryList]
print(groceryList)'''


'''⚔️ Mini Reiteration Challenge:
>> Create a list of your favorite three movies. Then:
>> Add one more using append().
>> Replace the second movie with "The Matrix".
>> Remove the last one using pop().
>> Check if "Inception" is in your list.
>> Convert all movie names to uppercase using a loop and print them.'''

'''movies = ["Coolie","F1","Leo"]
movies.append("Vikram")
print(movies)
movies[1] = "The Matrix"
print(movies)
movies.pop()
print(movies)
if "Inception" in movies:
    print("Inception is in movies list")
else:
    print("Inception is not in movies list")

i = 0
for movie in movies:
    movies[i] = movie.lower()
    i+=1

print(movies)'''


#slicing
#print(name[0:10:2])



#Tuples and dictionary

myTuple = (10,20,30,40)

#print(myTuple)

person = {
    name:"f{name}",
    age: "f{age}",
    "hobbies":"[Cricket, Code, gym]"
}

#print(person)

book = {
    "Title":"Harry Potter",
    "Author":"Krithik",
    "year":2025
}

'''for key,value in book.items():
    print(f"{key}: {value}")'''

book["genre"] = "Fiction"

#print(book)

def testArgs(*args):
    print(args)

def testKwargs(**kwargs):
    print(kwargs)

'''testArgs(1,2,3,4,5,6)
testKwargs(name="krithik",age=22,hobbies=['cricket','gym','code'])
'''
'''⚔️ Mini Challenge:
Write a function called log_expense that takes:
- A fixed argument date
- A variable number of *items (like food, transport, etc.)
- And keyword arguments **costs (like food=100, transport=50)'''

def logExpense(date,*items,**costs):
    print(f"on {date}\nItems: {items}\nCost: {costs}")

#logExpense('21-07-2025','food','transport','utils',food=200,transport=500,utils=300)

set = {1,2,3,4,5}
set.discard(6)

print(set)


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
print(matrix_1d)