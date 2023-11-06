#!/usr/bin/python3
"""Implementation of BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area method

        Args:
            None

        Raises:
            Exception: area() is not implemented

        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """integer validator

        Args:
            name (string): always a string
            value (int): always an int

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
