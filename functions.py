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
    
welcomUser("krithik")
print(squareIt(5))
print(chooseActivity("cold"))