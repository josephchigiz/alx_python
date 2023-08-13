#!/usr/bin/python3
"""Task 6"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # self.__name = name
        # self.__value = value

        if not type(value) is int:
            raise TypeError("{name} must be an integer")
        elif self.__value <= 0:
            raise ValueError("{name} must be greater than 0")

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        used_attr = []

        for att in attributes:
            if att != "__init_subclass__":
                used_attr.append(att)
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
        used_attr = []

        for att in attributes:
            if att != "__init_subclass__":
                used_attr.append(att)
        return used_attr


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        used_attr = []

        for att in attributes:
            if att != "__init_subclass__":
                used_attr.append(att)
        return used_attr
