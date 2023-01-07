#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Creation of first place --")

first_place = Place()
first_place.city_id = "f4d56z6s6z4f4z631"
first_place.name = "bella vista hotel"
first_place.description = "comfortable place for guests"
first_place.number_rooms = 4
first_place.number_bathrooms = 2
first_place.max_guest = 6
first_place.price_by_night = 400
first_place.latitude = 612.781
first_place.longitude = 286.125
first_place.amenity_ids = []
first_place.amenity_ids.append("k5fd4v5fs65f")
first_place.amenity_ids.append("ds56csdc5dsv")
first_place.save()
print(first_place)
