#!/usr/bin/python3
# Import the add function from add_0.py
from add_0 import add

# Define the variables a and b
a = 1
b = 2

# Call the add function with a and b as arguments and print the result
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
