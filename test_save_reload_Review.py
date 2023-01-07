#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Creation of first Review --")

first_review = Review()
first_review.place_id = "ds56sf4s5fvs54f"
first_review.user_id = "d65sf4csf4v6ds4f6z4f6s6dsfree"
first_review.text = 'just review of all we do it before'
first_review.save()
print(first_review)
