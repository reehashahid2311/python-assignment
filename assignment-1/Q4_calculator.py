def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b


while True:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    operation = input("Operation (+, -, *, /, %): ")

    if operation == "+":
        print("Result:", add(a, b))
    elif operation == "-":
        print("Result:", subtract(a, b))
    elif operation == "*":
        print("Result:", multiply(a, b))
    elif operation == "/":
        print("Result:", divide(a, b) if b != 0 else "Cannot divide by zero")
    elif operation == "%":
        print("Result:", modulus(a, b) if b != 0 else "Cannot use zero")
    else:
        print("Invalid operation")

    if input("Again? (yes/no): ").lower() != "yes":
        break
