#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Initialize an empty set to store unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for numb in my_list:
        unique_integers.add(numb)

    # Calculate the sum of unique integers in the set
    sum_unique = sum(unique_integers)

    return sum_unique
