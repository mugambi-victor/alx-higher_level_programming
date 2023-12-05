#!/usr/bin/python3
"""Student module
"""


class Student:
    """Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings
            specifying the attribute names
                to be included in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: A dictionary containing the
            specified attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing
            attribute names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """String representation of the Student instance.

        Returns:
            str: A formatted string
            containing information about the Student instance.
        """
        return "[Student] {} {} - {}".format(
                self.first_name, self.last_name, self.age)
