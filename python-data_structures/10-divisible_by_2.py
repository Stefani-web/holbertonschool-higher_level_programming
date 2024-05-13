#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True/False values
    result = []

# Iterate through the original list and check if each element is divisible by 2
    for numb in my_list:
        result.append(numb % 2 == 0)

    return result
