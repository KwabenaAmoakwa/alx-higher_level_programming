#!/usr/bin/python3
"""#!/usr/bin/python3 makes the file executable
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
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

    def area(self):
        """
        Method named area for calculatiing area of the square

        Return:
            area of square
        """
        return self.__size**2
