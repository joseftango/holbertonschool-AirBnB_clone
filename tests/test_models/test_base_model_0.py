#!/usr/bin/python3
import unittest
import uuid
from models import base_model
from datetime import datetime


class Test_BaseModel(unittest.TestCase):

    def test_save_method(self):
        model = base_model.BaseModel()
        updated_at_before_save = model.updated_at
        self.assertEqual(updated_at_before_save, model.updated_at)
        model.save()
        self.assertNotEqual(updated_at_before_save, model.updated_at)

    def test_to_dict_method(self):
        model = base_model.BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["id"], model.id, "ID in dict does not match model ID")
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat(), 
                         "created_at in dict does not match ISO format")
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat(), 
                         "updated_at in dict does not match ISO format")
        self.assertEqual(model_dict["__class__"], 'BaseModel')

    def test_Base_module_attributes(self):
        b = base_model.BaseModel()
        self.assertIsNotNone(b)
        self.assertIsInstance(b.id, str, "ID is not a string")

        uuid_obj = uuid.UUID(b.id)
        self.assertIsInstance(uuid_obj, uuid.UUID, "Generated object is not a UUID instance")
        self.assertEqual(uuid_obj.version, 4, "UUID version is not 4")

        self.assertIsInstance(b.created_at, datetime, "Generated object is not a datetime instance")

    def test_str_method(self):
        model = base_model.BaseModel()
        self.assertEqual(str(model), f'[{type(model).__name__}] ({model.id}) {model.__dict__}')
