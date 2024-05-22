#!/usr/bin/python3
"""This module defines the BaseGeometry class with specific methods"""


class BaseGeometry:
    def area(self):
        """Raises an Exception with the message
        "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer, raises a TypeError exception with
          the message "<name> must be an integer"
        - If value is less than or equal to 0, raises a ValueError exception
        with the message "<name> must be greater than 0"

        Args:
            name (str): The name of the value (assumed to be a string)
            value (int): The value to validate
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
