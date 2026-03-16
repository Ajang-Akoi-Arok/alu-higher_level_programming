#!/usr/bin/python3
"""
MyList module

This module defines a class MyList that inherits from the built-in list class.
It adds a method to print the list in sorted order without modifying the
original.
"""


class MyList(list):
    """
    A custom list class that inherits from Python's built-in list.

    This class inherits all functionality of the standard list class and adds
    a method to print the list in ascending sorted order.

    Methods:
        print_sorted(): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method creates a sorted copy of the list and prints it,
        leaving the original list unchanged. All elements in the list
        are assumed to be integers.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
