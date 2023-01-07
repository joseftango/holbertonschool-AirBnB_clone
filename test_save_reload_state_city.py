#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new State --")

my_state = State()
my_state.name = "Bahia"
my_state.save()
print(my_state)

print("-- Create a new City --")

my_city = City()
my_city.state_id = "51g564s84v56"
my_city.name = "El Salvador"
my_city.save()
print(my_city)

