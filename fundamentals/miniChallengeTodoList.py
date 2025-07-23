tasks = []
print("Welcome to your To-Do List Manager!\n1. Add Task\n2. View Tasks\n3.Remove Task\n4.Mark a task as done\n5. Quit")

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number choice")
        continue

    if choice == 1:
        task = input("Enter a task to add: ")
        if task not in tasks:
            tasks.append(task.lower())
            print("Task Added!")
        else:
            print("Task already in our To do")
    
    elif choice == 2:
        if not tasks:
            print("You do not have any tasks yet")
        else:
            print(f"Tasks:\n{tasks}")
    
    elif choice == 3:
        task = input("Enter a task to remove: ")
        if task.isdigit():
            task = int(task)
            tasks.pop(task-1)
        else:
            if task in tasks:
                tasks.remove(task.lower())
            else:
                print("No such task in you tasks list")
                continue;
    elif choice == 4:
        if not tasks:
            print("No tasks to mark as done")
        else:
            task = int(input("Enter a task number to mark as done:")) - 1
            tasks[task] = f"✔ {tasks[task]}"
        print(f"Tasks: {tasks}")
    elif choice == 5:
        break
    else:
        print("Enter a valid choice between 1-4")