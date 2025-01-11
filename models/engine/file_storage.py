#!/usr/bin/python3
'''file_storage module'''
from json import dump, load
from models import base_model
import os


class FileStorage:
    '''FileStorage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        '''serializes __objects to the JSON file'''
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            dump(self.__objects, f, indent=2)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                json_dict = load(f)
            for k, v in json_dict.items():
                my_model = base_model.BaseModel(**v)
                self.__objects[k] = str(my_model)

