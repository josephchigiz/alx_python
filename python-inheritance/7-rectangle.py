#!/usr/bin/python3
"""Task 7"""


class BaseGeometryMeta(type):
    """Meta Class for BAseGeometry"""

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr


class BaseGeometry(metaclass=BaseGeometryMeta):
    """BaseGeometry Class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        self.__name = name
        self.__value = value

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(self.__name))
        elif self.__value <= 0:
            raise ValueError("{} must be greater than 0".format(self.__name))

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr


class Rectangle(BaseGeometry):
    """Rectangle SubClass"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        area_rect = int(self.__width) * int(self.__height)
        return area_rect

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr
