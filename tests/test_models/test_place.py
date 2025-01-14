#!/usr/bin/python3
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    def test_Place_attributes(self):
        self.assertEqual(Place.name, '')
        self.assertEqual(Place.city_id, '')
        self.assertEqual(Place.user_id, '')
        self.assertEqual(Place.description, '')
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
