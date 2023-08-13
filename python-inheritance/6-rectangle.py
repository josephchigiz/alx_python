#!/usr/bin/python3
"""Task 6"""


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
        self.name = name
        self.value = value

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    """Rectangle SubClass"""

    def __init__(self, width, height):
        self.integer_validator("width", height)
        self.integer_validator("width", height)
        self.__width = width
        self.__height = height
