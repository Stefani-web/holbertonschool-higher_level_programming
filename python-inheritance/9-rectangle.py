#!/usr/bin/python3
"""This module contains the Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """This class represents a rectangle."""
def __init__(self, width, height):
        """
         Initializes a new instance of the Rectangle class.

         Args:
             width (int): The width of the rectangle.
             height (int): The height of the rectangle.
         """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)


def area(self):
        """ Returns the area of the rectangle"""
        return self.__width * self.__height


def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
