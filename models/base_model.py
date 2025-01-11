#!/usr/bin/python3
'''base_model module'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    '''BaseModel class'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''returns a string representation of the object'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''save method'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''converts the instance to dictionary'''
        my_dict = {}
        my_dict['__class__'] = self.__class__.__name__

        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v

        return my_dict
