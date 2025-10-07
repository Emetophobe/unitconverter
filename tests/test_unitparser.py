# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest
from fractions import Fraction

from unitconverter.exceptions import InvalidUnitError
from unitconverter.models.dimension import Dimension
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.registry import Registry

from tests import metre, second


class TestUnitParser(unittest.TestCase):
    """ Tests for the UnitParser class. """

    def setUp(self) -> None:
        registry = Registry([metre, second])
        self.parser = UnitParser(registry)

    def test__init__(self):
        # Invalid registry should raise a typeError
        with self.assertRaises(TypeError):
            UnitParser(None)  # type: ignore

    def test_parse_unit(self) -> None:
        # Invalid arguments should raise a TypeError
        with self.assertRaises(TypeError):
            self.parser.parse_unit(None)  # type: ignore

        # Undefined units should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            self.parser.parse_unit("undefined unit")

        # Test division
        unit = self.parser.parse_unit("m/s")
        self.assertEqual(unit.name, "metre/second")
        self.assertEqual(unit.factor, 1)
        self.assertEqual(unit.dimension, Dimension({"length": 1, "time": -1}))

        unit = self.parser.parse_unit("m/s/s")
        self.assertEqual(unit.name, "metre/second^2")
        self.assertEqual(unit.factor, 1)
        self.assertEqual(unit.dimension, Dimension({"length": 1, "time": -2}))

        # Test multiplication
        unit = self.parser.parse_unit("cm*s")
        self.assertEqual(unit.name, "centimetre*second")
        self.assertEqual(unit.factor, Fraction(1, 100))
        self.assertEqual(unit.dimension, Dimension({"length": 1, "time": 1}))

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
