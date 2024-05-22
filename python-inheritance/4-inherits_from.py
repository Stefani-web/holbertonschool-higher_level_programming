#!/usr/bin/python3
"""This module contains the `inherits_from` function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise False.
    """
    if isinstance(obj, bool):
        return False
    elif issubclass(type(obj), a_class):
        print(f"True inherited from class {a_class.__name__}")
        return True
    else:
        print("False")
        return False
