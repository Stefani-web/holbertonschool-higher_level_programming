#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b has fewer than 2 elements, fill with 0
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add corresponding elements from each tuple
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
