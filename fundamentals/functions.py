from functools import reduce


def welcomUser(name="there"):
    print(f"Hello {name}")

def squareIt(n):
    return n*n

def chooseActivity(weather):
    if weather == "sunny":
        return "Go for a walk"
    elif weather == "rainy":
        return "Read a book"
    else:
        return "Just Chill"
    
'''welcomUser("krithik")
print(squareIt(5))
print(chooseActivity("cold"))'''

# Functions that return multiple values
def getStats(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total/len(numbers)
    return total,avg

'''numbers = [10,20,30,40]
total, avg = getStats(numbers)
print(f"Total: {total}, Avg: {avg}")'''


#Mini Challenge
#Take a list of tasks and return 2 separate lists - Tasks done, Tasks yet to complete

'''def GimmeTasks(tasks):
    doneTasks = [task for task in tasks if "[x]" in task]
    incompleteTasks = [task for task in tasks if "[x]" not in task]
    return doneTasks, incompleteTasks

tasks = ["[x] wash dishes", "do homework", "[x] call mom", "write code"]
done,undone = GimmeTasks(tasks)

print(f"Done tasks: {done}\nUndone: {undone}")'''


#Lambda functions, it is like arrow functions in JS

add = lambda x,y:x+y
#print(add(2,3))


people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
#Sorts the list with their ages
people.sort(key=lambda x: x[1])


nums = [1, 2, 3, 4]
#map() applies a function to each item in a list.
squares = list(map(lambda x: x**2, nums))

nums = [1, 2, 3, 4, 5]
#filter() checks each item and keeps only the ones where the condition is True.
even = list(filter(lambda x: x % 2 == 0, nums))

# syntax for filter using lambda fn - filter(lambda name: <condition>, names)

'''
🧠 Challenge:
You're given a list of names. Filter only the names that start with the letter S (case-sensitive).
'''
names = ["Sai", "Karthik", "Surya", "Ravi", "Shiva", "Arjun"]

names_starting_w_s = list(filter(lambda x: x[0]=='S',names))

#print(names_starting_w_s)
words = ['apple', 'banana', 'apple', 'cherry', 'date', 'banana', 'elderberry']



#lessons of zip() and enumerate()
names = ["Krithik", "Dhoni", "Kohli"]
scores = [90, 85, 88]

#To create a dictionary where key is the name and value is the score

match_score = {name:score for name,score in zip(names,scores)}
print(match_score)


items = ["pen", "notebook", "eraser"]
#To create key - index and value - item
items_dict = {idx:item for idx,item in enumerate(items)}
print(items_dict)


subjects = ["Math", "Science", "History"]
marks = [78, 89, 91]

#To create a dictionary key - index and value - tuple like(Math, 78)

subject_mark = {idx:mark for idx,mark in enumerate(zip(subjects,marks))}
print(subject_mark)



#reduce() function

words = ["python", "reduce", "is", "awesome", "functional", "power"]
longest = reduce(lambda x,y:x if len(x) > len(y) else y,words)

print(longest)


'''
Input
words = ["apple", "banana", "grape"]
Output
{'a': 4, 'p': 3, 'l': 1, 'e': 2, 'b': 1, 'n': 2, 'g': 1, 'r': 1}
'''
