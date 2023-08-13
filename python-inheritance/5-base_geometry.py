#!/usr/bin/Python3
"""tASK 5"""


class BaseGeometry:
    """BaseGeometry Class"""

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
