#!/usr/bin/python3
"""city review"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""class named Review"""
	place_id = ""
	user_id = ""
	text = ""
