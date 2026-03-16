#!/usr/bin/python3
"""
BaseGeometry module

This module defines a class BaseGeometry with area method and integer validator.
"""


class BaseGeometry:
    """
    BaseGeometry class with area method and integer validator.

    This class provides basic geometry functionality including area calculation
    (to be implemented by subclasses) and integer validation.

    Methods:
        area(): Raises an exception indicating the method is not implemented.
        integer_validator(name, value): Validates that value is a positive int.
    """

    def area(self):
        """
        Public instance method that raises an Exception.

        This method should be overridden by subclasses to calculate area.

        Raises:
            Exception: Always raises an exception with message
                      "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
