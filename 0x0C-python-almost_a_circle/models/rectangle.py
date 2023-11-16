#!/usr/bin/python3
"""Implementation of rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from the Base class.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a
            Rectangle object with the specified width, height, coordinates,
            and optional ID.

    Properties:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the rectangle (default is 0).
            id (int, optional): An optional ID for the object.

        Raises:
            ValueError: If width, height, x, or y is less than 0.
            TypeError: If width, height, x, or y is not an integer.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        int: Width of the rectangle.

        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.
        """
        return self.__width

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
        self.__width = value

    @property
    def height(self):
        """
        int: Height of the rectangle.

        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.
        """
        return self.__height

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
        self.__height = value

    @property
    def x(self):
        """
        int: X-coordinate of the rectangle.

        Raises:
            ValueError: If x is less than 0.
            TypeError: If x is not an integer.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x property.

        Args:
            value (int): New x value.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        int: Y-coordinate of the rectangle.

        Raises:
            ValueError: If y is less than 0.
            TypeError: If y is not an integer.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y property.

        Args:
            value (int): New y value.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of rectangle

        Args:
            None

        Returns:
            int: area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__height):
            print("#"*self.__width)

    def __str__(self):
        """
        Display string version of class
        """
        s = f"{self.__x}/{self.__y}"
        li = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {s} - {li}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute

        Args:
            args (set): set of arguments
            kwargs (dictionary): set of key value pair arguments

        Returns:
            None
        """
        largs = list(args)
        if len(args) < 5:
            for i in range(5-len(args)):
                largs += ["l"]
        width = kwargs['width'] if 'width' in kwargs else largs[0]
        height = kwargs['height'] if 'height' in kwargs else largs[1]
        x = kwargs['x'] if 'x' in kwargs else largs[2]
        y = kwargs['y'] if 'y' in kwargs else largs[3]
        id = kwargs['id'] if 'id' in kwargs else largs[4]

        self.id = id if id != "l" else self.id
        self.__width = width if width != "l" else self.__width
        self.__height = height if height != "l" else self.__height
        self.__x = x if x != "l" else self.__x
        self.__y = y if y != "l" else self.__y
