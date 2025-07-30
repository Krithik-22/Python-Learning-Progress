'''Your Mini Challenge:
Build a simple calculator with:

+, -, *, / operations

Two number inputs

Handle:

Non-numeric input → ValueError

Division by 0 → ZeroDivisionError'''

#custom exception
class InvalidOperationException(Exception):
    pass

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculator():
    try:
        op = input("What do you want to do? ")
        if op in ['add','sub','multiply','divide']:
            n1,n2 = map(int,input("Enter two numbers: ").split())
        elif op in ['exit','quit']:
            return None,None
        else:
            raise InvalidOperationException
        op_value = 0
        if op == 'add':
            op_value = add(n1,n2)
        elif op == 'sub':
            op_value = subtract(n1,n2)
        elif op == 'multiply':
            op_value = multiply(n1,n2)
        elif op == 'divide':
            op_value = divide(n1,n2)
        else:
            print('Not a valid operation that you requrested')
        return op,op_value
    except ValueError:
        print('Enter a valid number to perform operations on!!')
        return None,None
    except ZeroDivisionError:
        print("You cannot enter zero as a denominator in a division operation!!")
        return None,None
    except InvalidOperationException:
        print('Enter a vlid operation to perform')
        return None,None

    finally:
        print("Operation Attemptedd!!!")

while True:
    op, op_value = calculator()
    if op not in ['quit','exit']:
        print(f"You have performed {op} and the value returned is {op_value}")
    else:
        print("Bubyee!!!")

    