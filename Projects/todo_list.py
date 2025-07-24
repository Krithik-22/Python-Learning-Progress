with open('todo_list.txt','w') as file:
    file.write("To Do List\n")

print("Hi!! Hope you are doin great\n1. Add a Task\n2. List the Tasks\n3. Mark Task as Done\n4. Clear Todo app\n5.. Exit\n")

def add_task():
    task = input('Enter the task to add to ToDo app: ')
    with open('todo_list.txt','a') as file:
        file.write(f"- {task}\n")
    print('Task Added!!!')
    return

def list_task():
    with open('todo_list.txt','r') as file:
        tasks = file.read()
        print(tasks)

def mark_task_as_done(t):
    with open('todo_list.txt','r+') as file:
        tasks = file.readlines()
        for i in range(len(tasks)):
            if t in tasks[i]:
                tasks[i] = tasks[i].rstrip() + "✔\n"
        file.seek(0)
        file.writelines(tasks)
        file.truncate()

def clear_todo():
    with open('todo_list.txt','w') as file:
        pass

while True:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add_task()
    elif choice == 2:
        list_task()
    elif choice == 3:
        task = input("Enter task to mark as done: ")
        mark_task_as_done(task)
    elif choice == 4:
        clear_todo()
    elif choice == 5:
        break
    else:
        print("Please enter a valid choice!!!")