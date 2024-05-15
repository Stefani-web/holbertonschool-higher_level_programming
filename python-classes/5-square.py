#!/usr/bin/python3
"""
A class used to represent a Square.

    Attributes

    size (int): The size of one side of the square.

    Methods

    area(): Returns the area of the square.
    my_print(): Prints the square with the character '#'.
"""


class Square:
    def __init__(self, size=0):
        """Initialize the square with a given size.

        Parameters
        size : (int, optional) size of one side of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.
        Returns

        int
            The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Param.:
            value [int] : The size of one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns

        int
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'.

        If the size of the square is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
