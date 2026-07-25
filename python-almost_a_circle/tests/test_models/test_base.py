#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_base_auto_id(self):
        """Test Base() assigns an ID automatically."""
        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_base_auto_id_increment(self):
        """Test Base() assigns auto ID + 1 of the previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_id_passed(self):
        """Test Base(89) saves the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dict(self):
        """Test Base.to_json_string([{'id': 12}])."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        """Test Base.to_json_string([{'id': 12}]) returns a string."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test Base.from_json_string('[{"id": 89}]')."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test Base.from_json_string returns a list."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)

    def test_rectangle_create_id_only(self):
        """Test Rectangle.create(**{'id': 89})."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_create_id_width(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1})."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_create_id_width_height(self):
        """Test Rectangle.create with id, width, height."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_rectangle_create_id_width_height_x(self):
        """Test Rectangle.create with id, width, height, x."""
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r = Rectangle.create(**d)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_rectangle_create_full(self):
        """Test Rectangle.create with id, width, height, x, y."""
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**d)
        expected = (89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), expected)

    def test_rectangle_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_empty(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_list(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 1', content)
        self.assertIn('"height": 2', content)

    def test_rectangle_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file_exists(self):
        """Test Rectangle.load_from_file() when file exists."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), str(r1))

    def test_square_create_id_only(self):
        """Test Square.create(**{'id': 89})."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_square_create_id_size(self):
        """Test Square.create(**{'id': 89, 'size': 1})."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_square_create_id_size_x(self):
        """Test Square.create with id, size, x."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_square_create_full(self):
        """Test Square.create with id, size, x, y."""
        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**d)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_list(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"size": 1', content)

    def test_square_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        s1 = Square(5, 9, 1)
        Square.save_to_file([s1])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), str(s1))


if __name__ == "__main__":
    unittest.main()
