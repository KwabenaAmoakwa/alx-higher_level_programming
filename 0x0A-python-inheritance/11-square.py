#!/usr/bin/python3
"""Implementation of square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, which is a special case of a rectangle.

    This class inherits from the Rectangle class and represents a square with
    equal width and height.

    Attributes:
        Inherited from the Rectangle class.

    """
    def __init__(self, size):
        """Initializes a Square instance with the provided size.

        Args:
            size (int): The size of the square.

        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__width * self.__height

    def __str__(self):
        """string representation of square class.

        Returns:
            string: string representation of square class

        """
        return "[Sqaure] {}/{}".format(self.__width, self.__height)
