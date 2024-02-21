#!/usr/bin/python3
"""Defines unittests for base.py"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_creation_class(unittest.TestCase):
    """Unittests for testing creation of the Base class."""
