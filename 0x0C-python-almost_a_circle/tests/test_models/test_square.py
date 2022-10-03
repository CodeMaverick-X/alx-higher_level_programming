#!/usr/bin/python3
"""
test module for square module
"""

import io
import contextlib
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testsquare(unittest.TestCase):
    """
    start of test
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_01(self):
        """test instance of square with correct id's"""
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(3)
        self.assertEqual(s2.id, 2)
        s3 = Square(5, 0, 0 , 12)
        self.assertEqual(s3.id, 12)

    def test_02(self):
        """test instance"""
        s1 = Square(1)
        self.assertEqual(type(s1), Square)

    def test_03(self):
        """test correct requied arguments for size, x, y"""
        s1 = Square(1, 5, 3)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 3)

    def test_04(self):
        """test wrong required arguments for size"""
        with self.assertRaises(TypeError) as x:
            r1 = Square("str", 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square([7, 5], 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square((7, 5), 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(7.5, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(float("nan"), 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(float("inf"), 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(float("-inf"), 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Square(0, 5, 3)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Square(-1, 5, 3)
        self.assertEqual("width must be > 0", str(x.exception))


    def test_05(self):
        """test wrong required arguments for x"""
        with self.assertRaises(TypeError) as x:
            r1 = Square(4, "str", 3)
        self.assertEqual("x must be an integer", str(x.exception))
       
        with self.assertRaises(TypeError) as x:
            r1 = Square(4, [7, 5], 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, (7, 5), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 7.5, 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, float("nan"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, float("inf"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, float("-inf"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Square(4, -1, 3)
        self.assertEqual("x must be >= 0", str(x.exception))


    def test_06(self):
        """test wrong requirments for y"""
        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, "str")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, [7, 5])
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, (7, 5))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, 7.5)
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, float("nan"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, float("inf"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Square(4, 5, float("-inf"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Square(4, 5, -1)
        self.assertEqual("y must be >= 0", str(x.exception))


    def test_12_1(self):
        """Test for update method on Square with wrong types."""

        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))

    def test_14_0(self):
        """Test for public method to_dictionary."""

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

    def test_14_1(self):
        """Test for public method to_dictionary with wrong args."""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1_dictionary = s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))

    def test_10_4(self):
        """Test Square for methods inherited from Rectangle."""

        s1 = Square(9)
        self.assertEqual(s1.area(), 81)
        s2 = Square(4, 1, 2, 5)
        s2.update(7)
        self.assertEqual(s2.id, 7)
        f = io.StringIO()
        s3 = Square(4)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)


if __name__ == '__main__':
    unittest.main()
