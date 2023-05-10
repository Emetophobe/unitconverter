# Copyright (c) 2022-2023 Mike Cunningham


import unittest

from unitconverter.exceptions import UnitError
from unitconverter.formatting import format_exponent
from unitconverter.parser import parse_unit


class TestParser(unittest.TestCase):
    """ Test parser module. """

    def test_parse_unit(self) -> None:
        """ Test parse_unit() function. """
        # Test parsing simple built-in units.
        metre = parse_unit('metre')
        self.assertEqual(metre.name, 'metre')

        # Test prefix generated units
        kilolitre = parse_unit('kilolitre')
        self.assertEqual(kilolitre.name, 'kilolitre')

        # Test symbol generated units
        unit = parse_unit('ml')
        self.assertEqual(unit.name, 'millilitre')

        # Test exponent generated units
        unit = parse_unit('kilometre3')
        self.assertEqual(unit.name, format_exponent('kilometre', 3))
        self.assertEqual(unit.dimension, format_exponent('length', 3))

        # Test composite units
        unit = parse_unit('N*m/s')
        self.assertEqual(unit.name, 'newton*metre/second')

        # Test invalid unit names
        with self.assertRaises(UnitError):
            parse_unit('invalid unit')

        # Test invalid prefixes (units that don't support prefix scaling)
        with self.assertRaises(UnitError):
            parse_unit('kilodegrees')

        # Test invalid prefixes (units that don't support that type of prefix)
        with self.assertRaises(UnitError):
            parse_unit('picobyte')
