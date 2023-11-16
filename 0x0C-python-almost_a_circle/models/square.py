#!/usr/bin/python3
"""Implementation of sqaure class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square.

    Args:
        None

    Returns:
        None
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Display string version of class
        """
        s = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {s} - {self.size}"

    @property
    def width(self):
        """
        int: Width of the square.
        """
        return self.size

    @width.setter
    def width(self, value):
        """
        Setter for the width property.

        Args:
            value (int): New width value.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.size = value

    @property
    def height(self):
        """
        int: Height of the rectangle.
        """
        return self.size

    @height.setter
    def height(self, value):
        """
        Setter for the height property.

        Args:
            value (int): New height value.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.size = value
