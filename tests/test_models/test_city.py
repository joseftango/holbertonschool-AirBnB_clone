#!/usr/bin/python3
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    def test_City_attributes(self):
        self.assertEqual(City.state_id, '')
        self.assertEqual(City.name, '')
