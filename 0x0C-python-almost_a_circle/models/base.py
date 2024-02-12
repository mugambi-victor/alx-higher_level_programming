#!/usr/bin/python3
"""Module that defines the Base class."""


import json
import csv
import turtle


class Base:
    """The Base class."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class.

        Args:
            id (int, optional): The id for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A string representing a
            list of dictionaries in JSON format.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    header = ["id", "size", "x", "y"]
                writer.writerow(header)
                for obj in list_objs:
                    writer.writerow([getattr(obj, attr) for attr in header])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file.

        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader, [])
                if cls.__name__ == "Rectangle"
                and header == ["id", "width", "height", "x", "y"]:
                    return [cls(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4]))
                            for row in reader]
                elif cls.__name__ == "Square" and header == ["id", "size", "x", "y"]:
                    return [cls(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.end_fill()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        turtle.exitonclick()
