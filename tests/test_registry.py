# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.exceptions import DuplicateUnitError, InvalidUnitError
from unitconverter.registry import Registry

from tests import metre, second


class TestRegistry(unittest.TestCase):
    """ Tests for the Registry class. """

    def setUp(self) -> None:
        self.registry = Registry()
        self.registry.add_unit(metre)

    def test_add_unit(self) -> None:
        self.registry.add_unit(second)

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_unit(None)  # type: ignore

        # Duplicate units should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            self.registry.add_unit(metre)

    def test_add_alias(self) -> None:
        self.registry.add_alias(metre, "new alias 1")

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_alias(None, "new alias 2")  # type: ignore

        # Invalid aliases should raise a TypeError
        with self.assertRaises(TypeError):
            self.registry.add_alias(metre, None)  # type: ignore

        # Duplicate aliases should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            self.registry.add_alias(metre, "metre")

    def test_get_unit(self) -> None:
        # TODO: this should probably raise a TypeError
        with self.assertRaises(InvalidUnitError):
            self.registry.get_unit(None)  # type: ignore

        # Invalid or undefined unit should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            self.registry.get_unit("invalid unit")

        unit1 = self.registry.get_unit("metre")
        unit2 = self.registry.get_unit("m")
        self.assertEqual(unit1, unit2)

        unit1 = self.registry.get_unit("centimetres")
        unit2 = self.registry.get_unit("cm")
        self.assertEqual(unit1, unit2)
