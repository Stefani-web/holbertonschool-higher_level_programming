#!/usr/bin/python3

def max_integer(my_list=[]):
    # If the list is empty, return None
    if not my_list:
        return None

    # Initialize the maximum integer with the first element of the list
    max_numb = my_list[0]

    # Iterate through the list to find the maximum integer
    for numb in my_list:
        if numb > max_numb:
            max_numb = numb

    return max_numb
