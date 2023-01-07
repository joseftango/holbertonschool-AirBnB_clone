#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a first Amenity --")

first_amenity = Amenity()
first_amenity.name = "convenience"
first_amenity.save()
print(first_amenity)

print("-- Create a second Amenity --")

second_amenity = Amenity()
second_amenity.name = "security"
second_amenity.save()
print(second_amenity)
