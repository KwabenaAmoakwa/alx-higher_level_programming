#!/usr/bin/python3
"""#!/usr/bin/python3 makes the file executable
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """
        Method named area for calculatiing area of the square

        Return:
            area of square
        """
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__size

    @size.setter
    def position(self, value):
        if (not type(value) is tuple or
                value[0] < 0 or
                value[1] < 0 or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
