# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.parsers.fileparser import FileParser
from unitconverter.registry import Registry


class TestFileParser(unittest.TestCase):
    """ Tests for the FileParser class. """

    def test_load_units(self):
        registry = Registry()
        self.assertEqual(len(registry.units), 0, "Registry should be empty")
        FileParser().load_units(registry)
        self.assertGreater(len(registry.units), 0, "Registry should have units")
