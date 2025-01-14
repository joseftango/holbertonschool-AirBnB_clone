#!/usr/bin/python3
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    def test_Review_attributes(self):
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')
