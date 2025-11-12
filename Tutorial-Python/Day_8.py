# Solution

a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))
operation = str(input("Enter a operation : "))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
elif operation == "//":
    print(a // b)
elif operation == "%":
    print(a % b)
elif operation == "**":
    print(a ** b)
else:
    print("No operation selected. Please restart calculator")
