#!/usr/bin/python3
"""implementation of the print square module"""

def print_square(size):
        """Prints a square made of '#' characters of the specified size.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If the input `size` is not an integer or if it is a
            float and less than 0.
            ValueError: If the input `size` is less than 0.
        """
        if not type(size) is int:
                raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        if type(size) is float and size < 0:
                raise TypeError("size must be an integer")
        for i in range(size):
                print("#" * size)
