#!/usr/bin/python3
"""class definition for Rectangle class"""


class Rectangle:
    """This class defines a rectangle

    Attributes:
        __width (int): Width of rectangle.
        __height (int) : height of rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with adustable width and height.

        Args:
            width (int, optional): Width of the rectangle.
            Defaults to 0.
            height (int, optional): height of the rectangle.
            Defaults to 0.

        """
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return o
        return 2 * (self.__width + self.__height)
