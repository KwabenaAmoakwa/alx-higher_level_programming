#!/usr/bin/python3
"""Implementation of Base class module"""


class Base:
    """
    Base class.

    Attributes:
            __nb_objects (int): A class variable to track the number of
            objects created.

    Methods:
        __init__(self, id=None): Initializes a Base object with an optional
        ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): An optional ID for the object.

        Note:
            If no ID is provided, the object's ID will be set using the class
            variable __nb_objects.

        Raises:
            ValueError: If an ID less than 0 is provided.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects