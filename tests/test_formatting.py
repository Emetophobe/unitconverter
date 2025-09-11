# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from fractions import Fraction

from unitconverter.formatting import (format_name, format_display_name,
                                      format_exponent, format_quantity)


class TestFormatting(unittest.TestCase):
    """ Test formatting functions. """

    def test_format_quantity(self) -> None:
        quantity = Fraction("0.05")
        self.assertEqual(format_quantity(quantity), "0.05")
        self.assertEqual(format_quantity(quantity, precision=1), "0.1")
        self.assertEqual(format_quantity(quantity, fraction=True), "1/20")
        self.assertEqual(format_quantity(quantity, exponent=True), "5e-2")

        quantity = Fraction(1234567)
        self.assertEqual(format_quantity(quantity, separators=True), "1,234,567")

    def test_format_name(self) -> None:
        units = [("metre", 1), ("second", -1)]
        self.assertEqual(format_name(units), "metre*second^-1")

        units = [("volt", 1), ("second", 1), ("metre", -2)]
        self.assertEqual(format_name(units), "volt*second*metre^-2")

    def test_format_display_name(self) -> None:
        units = [("metre", 1), ("second", -1)]
        self.assertEqual(format_display_name(units), "metre/second")

        units = [("volt", 1), ("second", 1), ("metre", -2)]
        self.assertEqual(format_display_name(units), "volt*second/metre^2")

    def test_format_exponent(self) -> None:
        self.assertEqual(format_exponent("metre", -1), "metre^-1")
        self.assertEqual(format_exponent("metre", 1), "metre")
        self.assertEqual(format_exponent("metre", 2), "metre^2")
