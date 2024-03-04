#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class TestConsole(unittest.TestCase):
    """Unittests for the console."""
    def setUp(self):
        """Set up the test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after the test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test help command."""
        self.console.onecmd("help")
        self.assertIn("Documented commands (type help <topic>):",
                mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command."""
        self.assertTrue(self.console.onecmd("quit"))
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command."""
        self.assertTrue(self.console.onecmd("EOF"))
        self.assertTrue(mock_stdout.getvalue() == "")

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_show(self):
        """Test show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_destroy(self):
        """Test destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertTrue(len(f.getvalue().strip()) == 0)

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update(self):
        """Test update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue("'name': 'test'" in f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test count command."""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")
        self.console.onecmd("create User")
        self.console.onecmd("create State")
        self.console.onecmd("create State")
        self.console.onecmd("create State")
        self.console.onecmd("count BaseModel")
        self.assertTrue("1" in mock_stdout.getvalue().strip())
        self.console.onecmd("count User")
        self.assertTrue("2" in mock_stdout.getvalue().strip())
        self.console.onecmd("count State")
        self.assertTrue("3" in mock_stdout.getvalue().strip())
        self.console.onecmd("count")
        self.assertTrue("6" in mock_stdout.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
