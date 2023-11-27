#!/usr/bin/python3

"""
Module: 4-rectangle

Defines a Rectangle class.

"""


class Rectangle:
    """
    The Rectangle class represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a
        new Rectangle instance.
        area(self): Computes and returns the area of the rectangle.
        perimeter(self): Computes and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string representation of the
        rectangle to recreate a new instance.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
