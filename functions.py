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

def GimmeTasks(tasks):
    doneTasks = [task for task in tasks if "[x]" in task]
    incompleteTasks = [task for task in tasks if "[x]" not in task]
    return doneTasks, incompleteTasks

tasks = ["[x] wash dishes", "do homework", "[x] call mom", "write code"]
done,undone = GimmeTasks(tasks)

print(f"Done tasks: {done}\nUndone: {undone}")