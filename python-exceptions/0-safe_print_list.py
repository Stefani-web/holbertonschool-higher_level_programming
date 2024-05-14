#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    # Try to print each list item in the range of x
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            elements_printed += 1
        except IndexError:
            break

    # Print a new line break after printing all elements
    print()

    return elements_printed
