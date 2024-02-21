#!/usr/bin/python3
"""Defines unittests for base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase(unittest.TestCase):
    """test on testbase"""


    def test_init_with_id(self):
        instance = Base(id=5)
        self.assertEqual(instance.id, 5)

    def test_init_without_id(self):
        instance = Base()
        self.assertEqual(instance.id, 1)

    def test_to_json_string(self):
        instance = Base()
        result = instance.to_json_string([{'key': 'value'}])
        self.assertEqual(result, '[{"key": "value"}]')

    def test_to_json_string_empty_list(self):
        instance = Base()
        result = instance.to_json_string([])
        self.assertEqual(result, '[]')

    def test_save_to_file(self):
        instance = Base()
        instance.save_to_file([instance])


    def test_from_json_string(self):
        instance = Base()
        result = instance.from_json_string('[{"key": "value"}]')
        self.assertEqual(result, [{'key': 'value'}])


if __name__ == '__main__':
    unittest.main()
