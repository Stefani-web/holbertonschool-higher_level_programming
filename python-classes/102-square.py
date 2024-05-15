#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compare inequality based on area."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Compare greater than based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Compare greater than or equal based on area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Compare less than based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Compare less than or equal based on area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
