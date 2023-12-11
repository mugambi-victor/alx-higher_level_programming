import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_constructor_no_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_constructor_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)
    def setUp(self):
        # Reset the global counter before each test
        Base._Base__nb_objects = 0
    def test_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_negative_id(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)
    

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
    
    def test_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_data(self):
        data = [{"key": "value"}, {"id": 1, "name": "example"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key": "value"}, {"id": 1, "name": "example"}]')

    def test_to_json_string_mix_types(self):
        data = [{"key": "value"}, 42, "hello"]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key": "value"}, 42, "hello"]')

    def test_to_json_string_nested_dicts(self):
        data = [{"key": {"nested": "value"}}, {"id": 1, "name": {"nested": "example"}}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key": {"nested": "value"}}, {"id": 1, "name": {"nested": "example"}}]')


    def test_create_rectangle(self):
        dummy_instance = Rectangle.create(width=10, height=5, x=2, y=3)
        self.assertIsInstance(dummy_instance, Rectangle)
        self.assertEqual(dummy_instance.width, 10)
        self.assertEqual(dummy_instance.height, 5)
        self.assertEqual(dummy_instance.x, 2)
        self.assertEqual(dummy_instance.y, 3)

    def test_create_square(self):
        dummy_instance = Square.create(size=7, x=1, y=2)
        self.assertIsInstance(dummy_instance, Square)
        self.assertEqual(dummy_instance.size, 7)
        self.assertEqual(dummy_instance.x, 1)
        self.assertEqual(dummy_instance.y, 2)

    def test_load_from_file_empty_file(self):
        empty_file_path = "Rectangle.json"
        with open(empty_file_path, "w") as file:
            file.write("[]")

        instances = Rectangle.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_data(self):
        data = [{"id": 1, "width": 10, "height": 5, "x": 2, "y": 3}, {"id": 2, "width": 7, "height": 7, "x": 1, "y": 2}]
        with open("Rectangle.json", "w") as file:
            file.write(Base.to_json_string(data))

        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertIsInstance(instances[1], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])

        with open("Rectangle.csv", "r") as file:
            lines = file.readlines()
            self.assertEqual(lines[0].strip(), "id,width,height,x,y")
            self.assertEqual(lines[1].strip(), "1,10,7,2,8")
            self.assertEqual(lines[2].strip(), "2,2,4,0,0")
if __name__ == '__main__':
    unittest.main()
