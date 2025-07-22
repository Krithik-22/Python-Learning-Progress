
#'r' - reads the file
with open("sample.txt","r") as file:
    content = file.read()
    #print(content)

#'w' - writes the file completely
with open('output.txt','w') as file:
    file.write("We are gonna rock with our python journey\n")
    file.write("We are gonna rock with whatever we do\n")

#'a' - appends more to the existing file or a new file
with open('output.txt','a') as file:
    file.write("Let's rock!!!!\n")

'''✅ Mini Challenge:
🔧 Task: Create a simple phonebook that:
- Takes name and number input from user
- Saves it to a .txt file line by line in Name - Number format
- Later reads the file and prints all saved contacts'''

def get_contact():
    name = input("Enter the name: ")
    while True:
        number = input("Enter the phone number: ")
        if len(number) == 10 and number.isdigit():
            return name, number
        else:
            print("Not a Valid number!!!")

def save_contact(name, number):
    with open('phonebook.txt','a') as file:
        file.write(f"{name}\t{number}\n")

def show_phonebook():
    with open('phonebook.txt','r') as file:
        content = file.read()
        print(content)

def update_contact():
    return

with open('phonebook.txt','w') as file:
        file.write(f"Name\tNumber\n")

while True:
    choice = int(input("What do you wanna do?\n1. Add a number to phonebook\n2. List the contacts in phonebook\n3. Press any button to exit\nEnter a Choice: "))
    if choice == 1:
        name, number = get_contact()
        save_contact(name,number)
    elif choice == 2:
        show_phonebook()
    else:
        break