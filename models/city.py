#!/usr/bin/python3
'''city module'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City class that inherits from BaseModel'''
    state_id = ''
    name = ''
