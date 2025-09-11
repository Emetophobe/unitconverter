# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from tests.mock_units import metre, second

from unitconverter.exceptions import InvalidUnitError
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.registry import Registry


class TestUnitParser(unittest.TestCase):
    """ Tests for the UnitParser class. """

    def setUp(self) -> None:
        self.registry = Registry([metre, second])
        self.parser = UnitParser(self.registry)

    def test__init__(self):
        # Invalid registry should raise a typeError
        with self.assertRaises(TypeError):
            UnitParser(None)  # type: ignore

    def test_parse_unit(self) -> None:
        # Invalid arguments should raise a TypeError
        for invalid_type in ("", 1, 3.14, [], (), {}):
            with self.assertRaises(TypeError):
                self.parser.parse_unit(invalid_type)  # type: ignore

        # Undefined units should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            self.parser.parse_unit("undefined unit")

        # Test division
        unit = self.parser.parse_unit("metre/s")
        self.assertTrue(unit.name, "metre/s")
        self.assertTrue(unit.factor, 1)
        self.assertTrue(unit.dimension, {"metre": 1, "second": -1})

        # Test multiplication
        unit = self.parser.parse_unit("metre*s")
        self.assertTrue(unit.name, "metre*s")
        self.assertTrue(unit.factor, 1)
        self.assertTrue(unit.dimension, {"metre": 1, "second": -1})

        # Test positive exponents
        unit1 = self.parser.parse_unit("metre")
        unit2 = self.parser.parse_unit("metre^1")
        self.assertEqual(unit1, unit2)

        unit1 = self.parser.parse_unit("metre²")
        unit2 = self.parser.parse_unit("metre^2")
        self.assertEqual(unit1, unit2)

        # Test negative exponents
        unit1 = self.parser.parse_unit("second⁻¹")
        unit2 = self.parser.parse_unit("second^-1")
        self.assertEqual(unit1, unit2)

    def test_simplify_unit(self) -> None:
        simplify_unit = self.parser._simplify_unit

        self.assertEqual(simplify_unit("metre¹"), "metre1")
        self.assertEqual(simplify_unit("metre⁻¹"), "metre-1")

    def test_split_exponent(self) -> None:
        split_exponent = self.parser._split_exponent

        self.assertEqual(split_exponent("metre"), ("metre", 1))
        self.assertEqual(split_exponent("metre¹"), ("metre", 1))
        self.assertEqual(split_exponent("metre⁻¹"), ("metre", -1))
