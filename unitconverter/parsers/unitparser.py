# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import re

from unitconverter.exceptions import ConverterError, InvalidUnitError
from unitconverter.models.unit import Unit
from unitconverter.registry import Registry


class UnitParser:
    """ Parse a unit string into a unit instance. """

    def __init__(self, registry: Registry) -> None:
        """ Create a unit parser. """
        if not isinstance(registry, Registry):
            raise TypeError(f"{registry!r} is not a valid unit registry")

        self.registry = registry

    def parse_unit(self, name: str | Unit) -> Unit:
        """ Parse a unit name into a unit instance.

        Parameters
        ----------
        name : str
            A unit name or composite unit name (i.e "J/kg")

        Returns
        -------
        Unit
            The unit instance
        """

        # Check if we already have a unit
        if isinstance(name, Unit):
            return name

        if not name or not isinstance(name, str):
            raise TypeError(f"{name!r} is not a valid unit name")

        simple_name = self._simplify_unit(name)

        # Check if the unit is in the registry
        try:
            return self.registry.get_unit(simple_name)
        except InvalidUnitError:
            pass

        unit = None

        # Parse units separated by division
        if "/" in simple_name:
            names = simple_name.split("/")

            # Get the units before the divisor
            unit = self._multiply_units(names.pop(0))

            # Get and divide the units after the divisor
            for units in names:
                unit /= self._multiply_units(units)

        # Parse units separated by multiplication
        elif "*" in simple_name:
            unit = self._multiply_units(simple_name)

        # Parse regular unit
        else:
            unit = self._parse_unit_name(simple_name)

        if not unit or not unit.name:
            raise InvalidUnitError(name)

        return unit

    def _parse_unit_name(self, name: str) -> Unit:
        """ Parse a unit string with potential exponent into a unit instance. """
        name, exponent = self._split_exponent(name)
        unit = self.registry.get_unit(name)

        if exponent == 1:
            return unit

        return unit ** exponent

    def _multiply_units(self, name: str) -> Unit:
        """ Parse a unit string with multiplication symbol into a composite unit. """
        units = None
        for name in name.split("*"):
            unit = self._parse_unit_name(name)

            # Check for temperature units which can't be composited
            if (unit.dimension.name == "temperature" and not unit.name.endswith("kelvin")
                    and not unit.name == "rankine"):
                raise ConverterError(f"{unit.name} cannot be composited with other units"
                                     " (only kelvin and rankine are currently supported)")

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
    _unit_pattern = r"(?P<unit>[a-zA-Z°Ωµ-]*[a-zA-Z°Ωµ ]+){1}"
    _exp_pattern = r"[\^]?(?P<exp>[-+]?[0-9]+)?"
    _pattern = re.compile(_unit_pattern + _exp_pattern)

    # Dictionary of replacements for internal lookup
    _replacements = {
        # simplify exponents
        "**": "",
        "^": "",
        "⁺": "",
        "⁻": "-",
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
