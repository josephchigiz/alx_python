"""Import Base"""
from models.base import Base


class Rectangle(Base):
    """Priv attributes
    Class constructor:
    args:
    width, height, x=0, y=0, id=None"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """To call parent class constructor"""
        super().__init__(id)

    @property
    def width(self):
        """Used to access width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the  width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """To access the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set  the heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """To access x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Now set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """To access y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Used to get y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Used to calculates the rectangle's area

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the Rectangle instance with the character #
        returns:
        prints in stdout #
        """
        for _ in range(self.__height):
            print("#" * self.__width)
            """This overrides the __str__ method
            returns:
            [Rectangle] (id) {x}/{y} - {width}/{height}"""

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
