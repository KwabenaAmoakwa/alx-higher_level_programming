#!/usr/bin/python3
"""#!/usr/bin/python3 makes the file executable
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int or float): The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a specified size.

        Args:
            size (int or float): The size of the square's sides.
        """
        self.__size = size
