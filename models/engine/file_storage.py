#!/usr/bin/python3
'''file_storage module'''
from json import dump, load
from os.path import exists
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    '''FileStorage class'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            new_dict = {}
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            dump(new_dict, f, indent=2)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists'''
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                json_obj = load(f)
                for k, v in json_obj.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
