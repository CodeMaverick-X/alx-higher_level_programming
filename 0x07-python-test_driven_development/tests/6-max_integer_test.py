#!/usr/bin/python3
"""
unittest for max integer module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer



class Testmax(unittest.TestCase):
    """
    testcase for max intiger function.
    """

    def test_max_int(self):
        """test wih a regular list of ints, returns max result"""

        result = max_integer([3, 4, 7, 8])
        self.assertEqual(result, 8)

    def test_not_int(self):
        """test not int and raises exception"""
        l = [1, 2, "n", 4, 5]
        self.assertRaises(TypeError, max_integer, l)

    def test_for_empty(self):
        """tests with an empty list, raises an excptn"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
