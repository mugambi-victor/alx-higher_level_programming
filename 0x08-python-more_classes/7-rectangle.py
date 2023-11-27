#!/usr/bin/python3
"""
Module: 7-rectangle

Defines a Rectangle class.

"""


class Rectangle:
    """
    The Rectangle class represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): The number of
        instances of the Rectangle class.
        print_symbol: The symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes
        a new Rectangle instance.
        area(self): Computes and returns the area of the rectangle.
        perimeter(self): Computes and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
        __repr__(self): Returns a string
        representation of the rectangle to recreate a new instance.
        __del__(self): Prints a message when an
        instance of Rectangle is deleted.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(
            [str(self.print_symbol) * self.__width
                for _ in range(self.__height)]
            )
            if self.__width != 0 and self.__height != 0
            else ""
            )

    def __repr__(self):
        """
        Returns a string representation of the
        rectangle to recreate a new instance.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the number of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
