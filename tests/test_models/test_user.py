#!/usr/bin/python3
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    def test_User_attributes(self):
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')
