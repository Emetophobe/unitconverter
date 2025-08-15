# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import re
import logging

from unitconverter.exceptions import ConverterError
from unitconverter.models.unit import CompositeUnit, UnitType
from unitconverter.registry import Registry


class UnitParser:
    """ Parse a unit string into a unit object. """

    def __init__(self, registry: Registry) -> None:
        """ Initialize unit parser. """
        self.registry = registry

    def parse_unit(self, name: str | UnitType) -> UnitType:
        """ Parse a string into a unit instance. Can be a composite unit.

        Parameters
        ----------
        `name` : str
            A unit name or composition of unit names (i.e "J/kg")

        Returns
        -------
        UnitType
            A Unit or a CompositeUnit.
        """

        # Check if we already have a unit
        if isinstance(name, UnitType):
            return name

        # Convert name into a simplied version
        name = _simplify_unit(name)

        # Try to parse the string into a unit
        try:
            return self._parse_unit_name(name)
        except ConverterError:
            pass

        # Try to create a composite unit
        return self._parse_composite_unit(name)

    def _parse_unit_name(self, name: str) -> UnitType:
        """ Parse a unit string into a unit instance. """

        # Check if name is in the registry
        try:
            return self.registry.get_unit(name)
        except ConverterError:
            pass

        # Check if name contains a mathematical expression (not valid here)
        if "*" in name or "/" in name:
            raise ConverterError(f"{name} is not a valid unit")

        # Finally, try to split the unit name and exponent
        try:
            name, exponent = _split_exponent(name)
            unit = self.registry.get_unit(name)

            if exponent != 1:
                return CompositeUnit(unit.factor, unit.name, unit.dimen) ** exponent
            else:
                return unit

        except ConverterError:
            raise ConverterError(f"{name} is not a valid unit")

    def _parse_composite_unit(self, name: str) -> UnitType:
        """ Parse a unit string into a composite unit. """
        unit = CompositeUnit()

        # Separate units by division
        if "/" in name:
            names = name.split("/")

            # Get the unit(s) before the divisor
            unit = self._multiply_units(names.pop(0))

            # Get and divide the other units after the divisor
            for name in names:
                unit /= self._multiply_units(name)

        # Separate units by multiplication
        elif "*" in name:
            unit = self._multiply_units(name)
        else:
            unit = self._parse_unit_name(name)

        logging.debug(f"parse_composite_unit() - {unit} ({unit.dimen!r})")

        if not unit:
            raise ConverterError(f"{name} is not a valid unit")

        return unit

    def _multiply_units(self, name: str) -> UnitType:
        """ Parse a string with multiplication symbol into a single unit. """
        units = CompositeUnit()
        for name in name.split("*"):
            unit = self._parse_unit_name(name)
            # Check for unsupported temperature units
            if unit.name in ("celsius", "fahrenheit", "rankine"):
                raise ConverterError(f"{unit.name} cannot be composited with other units"
                                     " (only kelvin is currently supported)")

            # Combine units
            units *= unit

        return units


def _split_exponent(name: str) -> tuple[str, int]:
    """ Split a unit name and exponent into a tuple.

    Examples
    --------

        >>> split_exponent("metre^2")
        ("metre", 2)

        >>> split_exponent("second")
        ("second", 1)

        >>> split_exponent("second-1")
        ("second", -1)
    """
    result = _pattern.match(_simplify_unit(name))

    if not result:
        raise ConverterError(f"{name} is not a valid unit")

    if result.group("exp"):
        return (result.group("unit"), int(result.group("exp")))
    else:
        return (result.group("unit"), 1)


def _simplify_unit(name: str) -> str:
    """ Simplify a unit name by replacing strings/characters.

    Examples
    --------

        >>> simplify_unit("Nm²/volt^2")
        "Nm2/volt2"

        >>> simplify_unit("joule per gram")
        "joule/gram"

    """
    if not isinstance(name, str):
        raise ConverterError(f"{name} is not a valid unit")

    for key, value in _replacements.items():
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
