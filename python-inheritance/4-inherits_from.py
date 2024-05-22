#!/usr/bin/python3
"""This module contains the `inherits_from` function"""


def inherits_from(obj, a_class):
    """
    Returns a list of strings indicating whether the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    """
    result = []
    for cls in type(obj).__mro__[1:]:
        if issubclass(cls, a_class):
            result.append(f"True inherited from class {cls.__name__}")
    return result
