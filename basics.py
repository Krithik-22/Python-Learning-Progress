#Learning about data types
name="Krithik"
age = 21
height = 6.3
isCool = True

#print(name, age, height, isCool)

#Mini challenge
userName = input("Enter your name: ")
userAge = int(input("Enter your age: "))
#print("Hello ", userName, ", In 5 years you will be ", userAge + 5)
print(f"Hello {userName}! In 5 years you will be {userAge + 5}")

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
haveVoterId = input("Do you have a Voter ID? ")

if userAge >= 18 and haveVoterId == 'yes':
    print('You are eligible to vote')
elif userAge >= 18 and haveVoterId == 'no':
    print('You are eligible to vote but you need a voter ID')
else:
    print('You cannot vote')