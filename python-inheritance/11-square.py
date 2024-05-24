#!/usr/bin/python3
"""
This module defines the `Square` class which inherits from `Rectangle`
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A `Square` class that inherits from `Rectangle`
    """

    def __init__(self, size):
        """
        Initializes a new instance of `Square`.

         Args:
             size (int): The size of the square. Must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a description of the square in the form [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
