# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import re

from unitconverter.exceptions import ConverterError, InvalidUnitError
from unitconverter.models.unit import BaseUnit, CompositeUnit
from unitconverter.registry import Registry


class UnitParser:
    """ Parse a unit string into a unit object. """

    def __init__(self, registry: Registry) -> None:
        """ Initialize unit parser. """
        self.registry = registry

    def parse_unit(self, name: str | BaseUnit) -> BaseUnit:
        """ Parse a string into a unit instance. Can be a composite unit.

        Parameters
        ----------
        name : str
            A unit name or composition of unit names (i.e "J/kg")

        Returns
        -------
        BaseUnit
            A Unit or a CompositeUnit.
        """

        # Check if we already have a unit
        if isinstance(name, BaseUnit):
            return name

        if not isinstance(name, str):
            raise ConverterError(f"{name!r} is not a string")

        # Try to parse a composite unit
        simple_name = self._simplify_unit(name)
        if "*" in simple_name or "/" in simple_name:
            return self._parse_composite_unit(name)

        # Try to parse a unit with optional exponent
        return self._parse_unit_name(name)

    def _parse_unit_name(self, name: str) -> BaseUnit:
        """ Parse a unit string with potential exponent into a unit instance. """
        name, exponent = self._split_exponent(name)
        unit = self.registry.get_unit(name)

        if exponent != 1:
            return CompositeUnit([(unit, exponent)])

        return unit

    def _parse_composite_unit(self, name: str) -> BaseUnit:
        """ Parse a unit string into a composite unit. """

        simple_name = self._simplify_unit(name)
        unit = None

        # Separate units by division
        if "/" in simple_name:
            names = simple_name.split("/")

            # Get the unit(s) before the divisor
            unit = self._multiply_units(names.pop(0))

            # Get and divide the other units after the divisor
            for units in names:
                unit /= self._multiply_units(units)

        # Separate units by multiplication
        elif "*" in simple_name:
            unit = self._multiply_units(simple_name)
        else:
            unit = self._parse_unit_name(simple_name)

        if not unit:
            raise InvalidUnitError(name)

        return unit

    def _multiply_units(self, name: str) -> BaseUnit:
        """ Parse a string with multiplication symbol into a composite unit. """
        units = None
        for name in name.split("*"):
            unit = self._parse_unit_name(name)
            # Check for temperature units which can't be composited
            if unit.name in ("celsius", "fahrenheit", "rankine"):
                raise ConverterError(f"{unit.name} cannot be composited with other units"
                                     " (only kelvin is currently supported)")

            if units is None:
                units = unit
            else:
                units *= unit

        if not units:
            raise InvalidUnitError(name)

        return units

    def _split_exponent(self, name: str) -> tuple[str, int]:
        """ Split a unit name and exponent into a 2-tuple. """
        result = self._pattern.match(self._simplify_unit(name))
        if not result:
            raise InvalidUnitError(name)

        if result.group("exp"):
            return (result.group("unit"), int(result.group("exp")))
        else:
            return (result.group("unit"), 1)

    def _simplify_unit(self, name: str) -> str:
        """ Simplify a unit name by replacing strings orcharacters. """
        for key, value in self._replacements.items():
            if key in name:
                name = name.replace(key, value)

        return name

    # Unit name and exponent patterns
    _unit_pattern = r"(?P<unit>[a-zA-Z°Ωµ-]*[a-zA-Z°Ωµ]+){1}"
    _exp_pattern = r"[\^]?(?P<exp>[-+]?[0-9]+)?"
    _pattern = re.compile(_unit_pattern + _exp_pattern)

    # Dictionary of replacements for internal lookup
    _replacements = {
        # simplify exponents
        "^": "",
        "⁰": "0",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁷": "7",
        "⁸": "8",
        "⁹": "9",

        # simplify multiplication
        "⋅": "*",

        # simplify division (convert "metre per second" to "metre/second")
        " per ": "/",

        # regional spelling (this is easier than adding additional aliases)
        "meter": "metre",
        "liter": "litre",
    }
