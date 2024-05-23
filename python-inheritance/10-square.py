#!/usr/bin/python3
"""This module contains the Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square"""
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
