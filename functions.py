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