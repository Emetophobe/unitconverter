# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from fractions import Fraction

from unitconverter.converter import UnitConverter
from unitconverter.exceptions import IncompatibleUnitError, InvalidUnitError


class TestUnitConverter(unittest.TestCase):
    """ Tests for the UnitConverter class. """

    def setUp(self) -> None:
        self.converter = UnitConverter()

    def test_convert(self) -> None:
        test_value = Fraction(1)

        # Invalid quantities should raise a TypeError
        for quantity in (None, "", [""], [], (), {}, 3.14, "1.a"):
            with self.assertRaises(TypeError):
                self.converter.convert(quantity, "metre", "metre")  # type: ignore

        # Invalid units should raise a TypeError
        for unit in (None, "", [""], [], (), {}, 1, 3.14):
            with self.assertRaises(TypeError):
                self.converter.convert(test_value, unit, "metre")  # type: ignore
            with self.assertRaises(TypeError):
                self.converter.convert(test_value, "metre", unit)  # type: ignore

        # Undefined units should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            self.converter.convert(test_value, "undefined unit", "metre")  # type: ignore
        with self.assertRaises(InvalidUnitError):
            self.converter.convert(test_value, "metre", "undefined unit")  # type: ignore

        # Incompatible units should raise an IncompatibleUnitError
        with self.assertRaises(IncompatibleUnitError):
            self.converter.convert(test_value, "metre", "second")

        test_value = Fraction(1)
        tests = si_unit_tests + length_tests + us_volume_tests + temperature_tests

        # Test some conversions for expected values
        for (source, targets, expected) in tests:
            if isinstance(targets, str):
                targets = [targets]

            for target in targets:
                result = self.converter.convert(test_value, source, target)
                expected = Fraction(expected)
                self.assertEqual(result, expected,
                                 f"Invalid conversion between {source} and {target}"
                                 f" ({result} vs {expected})")

    def test_convert_temperature(self) -> None:
        test_value = Fraction(1)
        for (source, targets, expected) in temperature_tests:
            if isinstance(targets, str):
                targets = [targets]

            for target in targets:
                result = self.converter.convert_temperature(test_value, source, target)
                expected = Fraction(expected)
                self.assertEqual(result, expected,
                                 f"Invalid conversion between {source} and {target}"
                                 f" ({result} vs {expected})")


# Conversion tests

si_unit_tests = [
    ("newton", ["kg*m/s^2"], 1),
    ("pascal", ["N/m²"], 1),
    ("joule", ["m⋅N", "C⋅V", "W⋅s"], 1),
    ("watt", ["J/s", "V⋅A"], 1),
    ("coulomb", ["s⋅A", "F⋅V"], 1),
    ("volt", ["W/A", "J/C"], 1),
    ("farad", ["C/V", "s/Ω"], 1),
    # ohm requires 1/s which isn't implemented
    # siemes requires 1/Ω which isn't implemented
    ("weber", ["J/A", "T⋅m2", "V⋅s"], 1),
    ("tesla", ["V⋅s/m²", "Wb/m^2"], 1),
    ("henry", ["V⋅s/A", "Ω⋅s", "Wb/A"], 1)
]

length_tests = [
    ("league", "mile", 3),
    ("mile", "chain", 80),
    ("chain", "rod", 4),
    ("rod", "link", 25),
    ("fathom", "yard", 2),
    ("yard", "foot", 3),
    ("foot", "inch", 12),
    ("inch", "thou", 1000),
    ("inch", "cm", "2.54")
]

# Source: https://en.wikipedia.org/wiki/Cubic_inch#Equivalence_with_other_units_of_volume
us_volume_tests = [
    ("inch^3", "ft^3", "1/1728"),
    ("inch^3", "usgal", "1/231"),
    ("inch^3", "usquart", "4/231"),
    ("inch^3", "uspint", "8/231"),
    ("inch^3", "usgill", "32/231"),
    ("inch^3", "usfloz", "128/231"),
    ("inch^3", "ustbsp", "256/231"),
    ("inch^3", "ustsp", "256/77"),
    ("inch^3", "usbushel", "50/107521"),
    ("inch^3", "usdryquart", "1600/107521"),
    ("inch^3", "usdrypint", "3200/107521"),
    ("inch^3", "mL", "16.387064")
]

temperature_tests = [
    ("kelvin", "celsius", "-272.15"),
    ("kelvin", "fahrenheit", "-457.87"),
    ("kelvin", "rankine", "1.8"),
    ("celsius", "kelvin", "274.15"),
    ("celsius", "fahrenheit", "33.8"),
    ("fahrenheit", "celsius", "-155/9"),
    ("fahrenheit", "kelvin", "46067/180"),
    ("rankine", "kelvin", "5/9"),
    ("kilokelvin", "kilocelsius", "0.72685")
]
