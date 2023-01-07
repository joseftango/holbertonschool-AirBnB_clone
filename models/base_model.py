#!/usr/bin/python3
"""model named: base_model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''class named BaseModel'''
    def __init__(self, **kwargs):
        '''constractor function'''
        if kwargs.__len__() > 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.fromisoformat(v))
                elif k == '__class__':
                    continue
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''method that return a string representation'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''method that updates the public instance attribute'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''method that returns a dictionary'''
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
