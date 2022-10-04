#!/usr/bin/python3
"""
test module for base module
"""


import unittest
from models.base import Base
import io
import contextlib

class testbase(unittest.TestCase):
    """
    start of test
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_01(self):
        """test instance of base with correct id's"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_02(self):
        """test instance"""
        b1 = Base()
        self.assertEqual(type(b1), Base)


    def test_03(self):
        """test to_json_string"""

        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")


