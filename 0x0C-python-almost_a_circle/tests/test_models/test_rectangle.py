#!/usr/bin/python3
"""
test module for rectangle module
"""

import io
import contextlib
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testrectangle(unittest.TestCase):
    """
    start of test
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_01(self):
        """test instance of rectangle with correct id's"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(5, 6, 0, 0 , 12)
        self.assertEqual(r3.id, 12)

    def test_02(self):
        """test instance"""
        r1 = Rectangle(1, 2)
        self.assertEqual(type(r1), Rectangle)

    def test_03(self):
        """test correct requied arguments for width, height, x, y"""
        r1 = Rectangle(1, 2, 5, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 3)

    def test_04(self):
        """test wrong requied arguments for width"""
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle("str", 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle([7, 5], 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle((7, 5), 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(7.5, 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(float("nan"), 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(float("inf"), 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(float("-inf"), 2, 5, 3)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(0, 2, 5, 3)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(-1, 2, 5, 3)
        self.assertEqual("width must be > 0", str(x.exception))


    def test_05(self):
        """test wrong requirments for height"""
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, "str", 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, [7, 5], 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, (7, 5), 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 7.5, 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, float("nan"), 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, float("inf"), 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, float("-inf"), 5, 3)
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(4, 0, 5, 3)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(4, -1, 5, 3)
        self.assertEqual("height must be > 0", str(x.exception))


    def test_06(self):
        """test wrong required arguments for x"""
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, "str", 3)
        self.assertEqual("x must be an integer", str(x.exception))
       
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, [7, 5], 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, (7, 5), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 7.5, 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, float("nan"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, float("inf"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, float("-inf"), 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(4, 2, -1, 3)
        self.assertEqual("x must be >= 0", str(x.exception))


    def test_07(self):
        """test wrong requirments for y"""
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, "str")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, [7, 5])
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, (7, 5))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, 7.5)
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, float("nan"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, float("inf"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(4, 2, 5, float("-inf"))
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r1 = Rectangle(4, 2, 5, -1)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_08(self):
        """test area method"""
        r1 = Rectangle(4, 2, 5, 3)
        area = r1.area()
        self.assertEqual(area, 8)

    def test_09(self):
        """Test for public method area with wrong args."""

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(3, 2)
            r1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(
                x.exception))
    

    def test_10(self):
        """test display method"""
        f = io.StringIO()
        r1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)
    
    def test_11(self):
        """test display wrong"""

        with self.assertRaises(TypeError) as x:
             r1 = Rectangle(9, 6)
             r1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_12(self):
        """Test for __str__ representation."""

        f = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(r1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_13(self):
        """Test for public method display with x and y."""

        f = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)






