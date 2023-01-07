#!/usr/bin/python3
import os
import json
"""importing models"""


class FileStorage:
	"""class named FileStorage"""
	__file_path = 'file.json'
	__objects = dict()

	def all(self):
		"""method that returns the dictionary __objects"""
		return self.__objects

	def	new(self, obj):
		"""method that sets in __objects the obj"""
		self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		with open(self.__file_path, 'w') as f:
			f.write(json.dumps(self.__objects, default=str))

	def reload(self):
		""" deserializes the JSON file to __objects"""
		if os.path.exists(self.__file_path):
			with open(self.__file_path, 'r') as f:
				self.__objects = json.load(f)
