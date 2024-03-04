#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_class_attribute(self):
        user_instance = User()
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(user_instance))
        self.assertNotIn("email", user_instance.__dict__)

    def test_password_is_public_class_attribute(self):
        user_instance = User()
        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(user_instance))
        self.assertNotIn("password", user_instance.__dict__)

    def test_first_name_is_public_class_attribute(self):
        user_instance = User()
        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(user_instance))
        self.assertNotIn("first_name", user_instance.__dict__)

    def test_last_name_is_public_class_attribute(self):
        user_instance = User()
        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(user_instance))
        self.assertNotIn("last_name", user_instance.__dict__)

    def test_two_users_unique_ids(self):
        user_instance1 = User()
        user_instance2 = User()
        self.assertNotEqual(user_instance1.id, user_instance2.id)

    def test_two_users_different_created_at(self):
        user_instance1 = User()
        sleep(0.05)
        user_instance2 = User()
        self.assertLess(user_instance1.created_at, user_instance2.created_at)

    def test_two_users_different_updated_at(self):
        user_instance1 = User()
        sleep(0.05)
        user_instance2 = User()
        self.assertLess(user_instance1.updated_at, user_instance2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user_instance = User()
        user_instance.id = "123456"
        user_instance.created_at = user_instance.updated_at = dt
        user_str = user_instance.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_args_unused(self):
        user_instance = User(None)
        self.assertNotIn(None, user_instance.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user_instance = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user_instance.id, "345")
        self.assertEqual(user_instance.created_at, dt)
        self.assertEqual(user_instance.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

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
        user_instance = User()
        sleep(0.05)
        first_updated_at = user_instance.updated_at
        user_instance.save()
        self.assertLess(first_updated_at, user_instance.updated_at)

    def test_two_saves(self):
        user_instance = User()
        sleep(0.05)
        first_updated_at = user_instance.updated_at
        user_instance.save()
        second_updated_at = user_instance.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user_instance.save()
        self.assertLess(second_updated_at, user_instance.updated_at)

    def test_save_with_arg(self):
        user_instance = User()
        with self.assertRaises(TypeError):
            user_instance.save(None)

    def test_save_updates_file(self):
        user_instance = User()
        user_instance.save()
        user_id = "User." + user_instance.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user_instance = User()
        self.assertIn("id", user_instance.to_dict())
        self.assertIn("created_at", user_instance.to_dict())
        self.assertIn("updated_at", user_instance.to_dict())
        self.assertIn("__class__", user_instance.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user_instance = User()
        user_instance.middle_name = "Holberton"
        user_instance.my_number = 98
        self.assertEqual("Holberton", user_instance.middle_name)
        self.assertIn("my_number", user_instance.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user_instance = User()
        user_dict = user_instance.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user_instance = User()
        user_instance.id = "123456"
        user_instance.created_at = user_instance.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user_instance.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        user_instance = User()
        self.assertNotEqual(user_instance.to_dict(), user_instance.__dict__)

    def test_to_dict_with_arg(self):
        user_instance = User()
        with self.assertRaises(TypeError):
            user_instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
