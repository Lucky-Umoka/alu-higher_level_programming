#!/usr/bin/python3
"""Unittest module for the Rectangle class."""
import unittest
import io
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_1_2(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_rectangle_1_2_3(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_rectangle_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_rectangle_width_str(self):
        """Test Rectangle("1", 2) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_height_str(self):
        """Test Rectangle(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_x_str(self):
        """Test Rectangle(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_y_str(self):
        """Test Rectangle(1, 2, 3, "4") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_1_2_3_4_5(self):
        """Test Rectangle(1, 2, 3, 4, 5) sets id."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_width_negative(self):
        """Test Rectangle(-1, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_height_negative(self):
        """Test Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_width_zero(self):
        """Test Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_height_zero(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_x_negative(self):
        """Test Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_y_negative(self):
        """Test Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test the area() method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test the __str__() method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        """Test display() without x and y."""
        r = Rectangle(2, 2)
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            r.display()
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Test display() without y."""
        r = Rectangle(2, 2, 1)
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            r.display()
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        """Test display() with x and y."""
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            r.display()
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary() in Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_no_args(self):
        """Test update() with no arguments."""
        r = Rectangle(10, 10, 10, 10)
        original = str(r)
        r.update()
        self.assertEqual(str(r), original)

    def test_update_89(self):
        """Test update(89) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_89_1_2_3_4(self):
        """Test update(89, 1, 2, 3, 4) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        result = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(result, (89, 1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test update(**{'id': 89, 'width': 1}) in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        """Test update with id, width, height kwargs in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        """Test update with id, width, height, x kwargs in Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r.update(**d)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_full(self):
        """Test update with id, width, height, x, y kwargs."""
        r = Rectangle(10, 10, 10, 10)
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r.update(**d)
        result = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(result, (89, 1, 2, 3, 4))


if __name__ == "__main__":
    unittest.main()
