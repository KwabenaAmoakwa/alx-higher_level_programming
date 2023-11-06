#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Prints the list in sorted order.

    Prints the elements of the list in ascending order using the sorted()
    function.

    Args:
        None

    Returns:
        None

    """
    def print_sorted(self):
        print(sorted(self))
