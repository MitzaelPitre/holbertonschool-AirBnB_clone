#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        base_model_instance = BaseModel()
        base_model_instance.id = "123456"
        base_model_instance.created_at = base_model_instance.updated_at = dt
        base_model_str = base_model_instance.__str__()
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn("'created_at': " + dt_repr, base_model_str)
        self.assertIn("'updated_at': " + dt_repr, base_model_str)

    def test_args_unused(self):
        base_model_instance = BaseModel(None)
        self.assertNotIn(None, base_model_instance.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model_instance = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model_instance.id, "345")
        self.assertEqual(base_model_instance.created_at, dt)
        self.assertEqual(base_model_instance.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        base_model_instance = BaseModel()
        sleep(0.05)
        first_updated_at = base_model_instance.updated_at
        base_model_instance.save()
        self.assertLess(first_updated_at, base_model_instance.updated_at)

    def test_two_saves(self):
        base_model_instance = BaseModel()
        sleep(0.05)
        first_updated_at = base_model_instance.updated_at
        base_model_instance.save()
        second_updated_at = base_model_instance.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_model_instance.save()
        self.assertLess(second_updated_at, base_model_instance.updated_at)

    def test_save_with_arg(self):
        base_model_instance = BaseModel()
        with self.assertRaises(TypeError):
            base_model_instance.save(None)

    def test_save_updates_file(self):
        base_model_instance = BaseModel()
        base_model_instance.save()
        base_model_id = "BaseModel." + base_model_instance.id
        with open("file.json", "r") as f:
            self.assertIn(base_model_id, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base_model_instance = BaseModel()
        self.assertIn("id", base_model_instance.to_dict())
        self.assertIn("created_at", base_model_instance.to_dict())
        self.assertIn("updated_at", base_model_instance.to_dict())
        self.assertIn("__class__", base_model_instance.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        base_model_instance = BaseModel()
        base_model_dict = base_model_instance.to_dict()
        self.assertEqual(str, type(base_model_dict["id"]))
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        base_model_instance = BaseModel()
        base_model_instance.id = "123456"
        base_model_instance.created_at = base_model_instance.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(base_model_instance.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        base_model_instance = BaseModel()
        self.assertNotEqual(base_model_instance.to_dict(), base_model_instance.__dict__)

    def test_to_dict_with_arg(self):
        base_model_instance = BaseModel()
        with self.assertRaises(TypeError):
            base_model_instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
