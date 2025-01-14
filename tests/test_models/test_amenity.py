#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    def test_Amenity_attributes(self):
        self.assertEqual(Amenity.name, '')
