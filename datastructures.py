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

text = input("Enter a sentence:")

text = text.split()
'''
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

print(unique)