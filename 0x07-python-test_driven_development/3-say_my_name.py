#!/usr/bin/python3
"""module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name based on the provided first name and last name.

    Arg:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
        TypeError: If the input first_name or last_name is not a string.

    Example:
        say_my_name("John", "Doe")  # Output: My name is John Doe
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
