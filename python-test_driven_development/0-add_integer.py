#!/usr/bin/env python3
def add_integer(a, b=98):
    """
    Adds two integers together

    Args:
        a (int or float): the first integer to add
        b (int or float, optional): the second integer to add. Defaults to 98

    Raises:
        TypeError: if a or b is not an integer or a float

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
