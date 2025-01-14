#!/usr/bin/python3
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    def test_State_attributes(self):
        self.assertEqual(State.name, '')
