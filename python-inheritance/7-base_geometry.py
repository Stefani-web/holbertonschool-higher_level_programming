#!/usr/bin/python3
"""7-base_geometry.py This module initializes a class called BaseGeometry"""


class BaseGeometry:
    """The 'BaseGeometry' class"""

    def __init__(self):
        """Initialize the class"""
        pass

    def area(self):
        """
        Instance method: def area(self):
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Instance method that validates value:
        Raise a TypeError if value is not an int
        Raise a ValueError if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
