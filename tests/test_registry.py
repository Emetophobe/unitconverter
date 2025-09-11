# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from tests.mock_units import metre

from unitconverter.exceptions import DuplicateUnitError, InvalidUnitError
from unitconverter.registry import Registry


class TestRegistry(unittest.TestCase):
    """ Tests for the Registry class. """

    def setUp(self) -> None:
        self.registry = Registry()

    def test___init__(self) -> None:
        self.assertEqual(len(self.registry.units), 0, "Default registry should have 0 units")

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            Registry("not a list of units")  # type: ignore

        # Duplicate units should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            Registry([metre, metre])

    def test_add_unit(self) -> None:
        self.registry.add_unit(metre)

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_unit("not a unit")  # type: ignore

        # Duplicate units should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            self.registry.add_unit(metre)

    def test_add_alias(self) -> None:
        self.registry.add_unit(metre)
        self.registry.add_alias("test_alias", metre)

        # Invalid alias should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_alias(None, metre)  # type: ignore

        # Invalid unit should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_alias("test_alias", None)  # type: ignore

        # Duplicate aliases should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            self.registry.add_alias("metre", metre)

    def test_get_unit(self) -> None:
        self.registry.add_unit(metre)

        # TODO: this should probably raise a TypeError
        with self.assertRaises(InvalidUnitError):
            self.registry.get_unit(3.14)  # type: ignore

        # Invalid or undefined unit should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            self.registry.get_unit("invalid unit")

        unit1 = self.registry.get_unit("metre")
        unit2 = self.registry.get_unit("m")
        self.assertEqual(unit1, unit2)

        unit1 = self.registry.get_unit("centimetres")
        unit2 = self.registry.get_unit("cm")
        self.assertEqual(unit1, unit2)
