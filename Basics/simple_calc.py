'''Q6: Simple Calculator

Write a program that:

1. Takes two numbers as input from the user.

2. Prints their sum, difference, product, and quotient.'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division by zero is not allowed.")