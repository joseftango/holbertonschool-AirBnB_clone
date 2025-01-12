#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os.path import exists
from os import remove
from json import load


class Test_FileStorage(unittest.TestCase):
    def setUp(self):
        """Clear storage before each test."""
        storage.all().clear()  # Clear all objects in storage
        if exists("file.json"):
            remove("file.json")

    # def test_File_Storage_all_attributes(self):

    #     with self.assertRaises(AttributeError) as context:
    #         path = storage.__file_path
    #     self.assertEqual(str(context.exception), "'FileStorage' object has no attribute '_Test_BaseModel__file_path'")

    #     with self.assertRaises(AttributeError) as context:
    #         objs = storage.__objects
    #     self.assertEqual(str(context.exception), "'FileStorage' object has no attribute '_Test_BaseModel__objects'")

    def test_empty_storage(self):
        all_objs = storage.all()
        self.assertEqual(all_objs, {})
        self.assertFalse(exists('file.json'))

    def test_File_Storage_all_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        my_model_key = f'{type(my_model).__name__}.{my_model.id}'
        self.assertEqual(my_model.id, all_objs[my_model_key].id)
        self.assertEqual(my_model.name, all_objs[my_model_key].name)
        self.assertEqual(my_model.my_number, all_objs[my_model_key].my_number)
        self.assertEqual(my_model.created_at, all_objs[my_model_key].created_at)
        self.assertEqual(my_model.updated_at, all_objs[my_model_key].updated_at)
        self.assertEqual(my_model.__class__, all_objs[my_model_key].__class__)

    def test_File_Storage_new_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        my_objects = storage.all()
        my_obj_key = f'{my_model.__class__.__name__}.{my_model.id}'
        self.assertEqual(my_model.id, my_objects[my_obj_key].id)
        self.assertEqual(my_model.name, my_objects[my_obj_key].name)
        self.assertEqual(my_model.my_number, my_objects[my_obj_key].my_number)
        self.assertEqual(my_model.created_at, my_objects[my_obj_key].created_at)
        self.assertEqual(my_model.updated_at, my_objects[my_obj_key].updated_at)
        self.assertEqual(my_model.__class__, my_objects[my_obj_key].__class__)

    def test_save_method_of_Base(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json", "r") as file:
            my_objects = load(file)
        my_obj_key = f'{my_model.__class__.__name__}.{my_model.id}'
        self.assertEqual(my_model.to_dict(), my_objects[my_obj_key])

    def test_File_storage_save_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()
        self.assertTrue(exists("file.json"))
        with open("file.json", "r") as file:
            my_objects = load(file)

        my_obj_key = f'{my_model.__class__.__name__}.{my_model.id}'
        self.assertEqual(my_model.to_dict(), my_objects[my_obj_key])

    def test_File_storage_reload_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.reload()
        my_objects = storage.all()
        my_obj_key = f'{my_model.__class__.__name__}.{my_model.id}'
        self.assertEqual(my_model.to_dict(), my_objects[my_obj_key].to_dict())

    def test_constractor_method_of_BaseModel(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_args = my_model.to_dict()

        new_model = BaseModel(**my_args)
        self.assertEqual(my_model.to_dict(), new_model.to_dict())
