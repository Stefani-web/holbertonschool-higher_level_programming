#!/usr/bin/python3
"""This module contains the "inherits_from" function"""


def inherits_from(obj, a_class):
    """
     Checks if an object is an instance of a class that has inherited
     (directly or indirectly) of the specified class

     Args:
         obj: The object to check
         a_class: The class to check

     Returns:
         True if `obj` is an instance of a class that inherited from `a_class`,
         otherwise False
     """
    return isinstance(obj, a_class) and type(obj) is not a_class
