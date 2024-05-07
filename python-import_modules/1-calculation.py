#!/usr/bin/python3
if __name__ == '__main__':
    a = 10
    b = 5

        # Import specific functions from calculator_1.py
    from calculator_1 import add, sub, mul, div
        # Call the imported functions with a and b as arguments and print the results
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
