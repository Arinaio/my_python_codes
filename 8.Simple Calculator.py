"""A calculator that canadd, subtract, multiply, divide, calculate power, square root and remainder of two numbers. 
Each operation is its own function that takes two numbers and returns the result.Square root only needs one number."""
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "error: can't divide by zero!"
    else:
        return a/b
def power(a,b):
    return a**b
def square_root(a):
    if a<0:
        return "error: can't square root a negative number"
    else:
        return a**0.5
def remainder(a,b):
    if b==0:
        return "error: can't divide by zero!"
    else:
        return a%b
operation=input("Pick an operation(add, subtract, multiply, divide, power, square root, remainder): ").lower()
if operation== "square root":
    a=float(input("Enter a number: "))
    print(square_root(a))
else:
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
    if operation== "add":
        print(add(a, b))
    elif operation== "subtract":
        print(subtract(a, b))
    elif operation== "multiply":
        print(multiply(a, b))
    elif operation== "divide":
        print(divide(a, b))
    elif operation== "power":
        print(power(a, b))
    elif operation== "remainder":
        print(remainder(a, b))
    else:
        print("Invalid operation!")
