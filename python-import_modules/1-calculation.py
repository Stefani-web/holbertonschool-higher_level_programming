#!/usr/bin/python3
# Import specific functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define the variables a and b
a = 10
b = 5

# Call the imported functions with a and b as arguments and print the results
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
