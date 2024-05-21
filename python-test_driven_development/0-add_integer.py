#!/usr/bin/env python3
"""A function add_integer that adds 2 integers"""


def add_integer(a, b=98):
    """Returns: the sum of a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)
