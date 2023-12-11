#!/usr/bin/python3
"""Module that defines the Square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """The Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )


    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
