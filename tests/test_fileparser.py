# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.parsers.fileparser import FileParser


class TestFileParser(unittest.TestCase):
    """ Tests for the FileParser class. """

    def setUp(self) -> None:
        self.parser = FileParser()

    def test_create_registry(self):
        registry = self.parser.create_registry()
        self.assertGreater(len(registry.units), 0, "Registry should have pre-defined units")
