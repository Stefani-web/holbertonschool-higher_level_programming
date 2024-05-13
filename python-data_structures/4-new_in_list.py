#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    list_copy = my_list[:]
    # Replace element if index is in valid range
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element
    return list_copy
