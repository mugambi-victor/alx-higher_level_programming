import unittest
from models.square import Square
import io
from unittest.mock import patch


class TestSquare(unittest.TestCase):

    def test_str(self):
        square = Square(4, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 4")

    def test_update_args(self):
        square = Square(4, 2, 3, 1)
        square.update(5, 10, 10, 2)
        self.assertEqual(str(square), "[Square] (5) 10/10 - 2")

    def test_update_kwargs(self):
        square = Square(4, 2, 3, 1)
        square.update(id=5, x=10, y=10, size=2)
        self.assertEqual(str(square), "[Square] (5) 10/10 - 2")

    def test_to_dictionary(self):
        square = Square(4, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_display(self):
        square = Square(3, 10, 2, 5)
        expected_output = "  ###\n  ###\n  ###\n"  # Remove extra leading newline characters
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)



if __name__ == '__main__':
    unittest.main()
