#!/usr/bin/python3
"""Unittest module for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_1(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_square_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_square_str_size(self):
        """Test Square("1") raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_str_x(self):
        """Test Square(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        """Test Square(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        """Test Square(1, 2, 3, 4) sets id."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_negative_size(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test the __str__() method for Square."""
        s = Square(3, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 3")

    def test_to_dictionary(self):
        """Test to_dictionary() in Square."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_no_args(self):
        """Test update() with no arguments."""
        s = Square(5)
        original = str(s)
        s.update()
        self.assertEqual(str(s), original)

    def test_update_89(self):
        """Test update(89) in Square."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Square."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Square."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Square."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89}) in Square."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test update(**{'id': 89, 'size': 1}) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        """Test update with id, size, x kwargs in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_full(self):
        """Test update with id, size, x, y kwargs in Square."""
        s = Square(5)
        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s.update(**d)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))


if __name__ == "__main__":
    unittest.main()
