#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests for FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.fs = FileStorage()

    def tearDown(self):
        """Tear down the test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method."""
        self.assertEqual(type(self.fs.all()), dict)

    def test_new(self):
        """Test the new() method."""
        bm = BaseModel()
        self.fs.new(bm)
        key = bm.__class__.__name__ + "." + bm.id
        self.assertIn(key, self.fs.all())

    def test_save(self):
        """Test the save() method."""
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        with open("file.json", "r") as f:
            self.assertIn(bm.__class__.__name__ + "." + bm.id, f.read())

    def test_reload(self):
        """Test the reload() method."""
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        del self.fs.all()[bm.__class__.__name__ + "." + bm.id]
        self.assertEqual(len(self.fs.all()), 0)
        self.fs.reload()
        self.assertEqual(len(self.fs.all()), 1)


if __name__ == "__main__":
    unittest.main()
