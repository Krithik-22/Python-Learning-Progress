tasks = []
print("Welcome to your To-Do List Manager!\n1. Add Task\n2. View Tasks\n3.Remove Task\n4.Quit")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter a task to add: ")
        tasks.append(task.lower())
        print("Task Added!")
    if choice == 2:
        print(f"Tasks\n{tasks}")
    
    if choice == 3:
        task = input("Enter a task to remove: ")
        tasks.remove(task.lower())
    if choice == 4:
        break;