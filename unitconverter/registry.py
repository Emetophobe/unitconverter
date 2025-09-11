# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import json
import re

from fractions import Fraction
from pathlib import Path

from unitconverter.exceptions import ConverterError, DuplicateUnitError, InvalidUnitError
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import BaseUnit, Unit


class Registry:
    """ The registry is used to store and retrieve pre-defined units. """

    def __init__(self, units: list[BaseUnit] | None = None) -> None:
        """ Create a unit registry.

        If no units are specified defaults are loaded from the json files.

        Parameters
        ----------
        units : list[Unit] | None, optional
            A list of units, by default None
        """
        self.units: dict[str, BaseUnit] = {}

        if units is None:
            self._load_units()
        else:
            for unit in units:
                self.add_unit(unit)

    def add_unit(self, unit: BaseUnit) -> BaseUnit:
        """ Add a unit to the registry.

        Parameters
        ----------
        unit : Unit
            The unit instance
        """

        if not isinstance(unit, BaseUnit):
            raise TypeError(f"{unit!r} is not a valid unit")

        # Add all unit names
        for name in unit.names:
            self.add_alias(name, unit)

        # Also add prefixed versions if the unit supports it
        for prefix in get_prefixes(unit.prefixes):
            name = prefix.name + unit.name
            symbols = [prefix.symbol + symbol for symbol in unit.symbols]
            aliases = [prefix.name + alias for alias in unit.aliases]
            factor = prefix.factor * unit.factor

            # Make sure prefixes=None to prevent re-prefixing and infinite recursion
            self.add_unit(Unit(name, symbols, aliases, unit.dimension, factor, prefixes=None))

        return unit

    def add_alias(self, alias: str, unit: str | BaseUnit) -> None:
        """ Add a unit alias.

        Parameters
        ----------
        alias : str
            Name, symbol, or alias

        unit : str | Unit
            The unit to alias
        """

        if not isinstance(alias, str) or not alias:
            raise TypeError(f"{alias!r} is not a valid unit alias")

        # Try to get a unit if we don't already have one
        if not isinstance(unit, Unit):
            unit = self.parse_unit(unit)

        if alias in self.units:
            raise DuplicateUnitError(alias, self.units[alias].name)

        # Add the reference
        self.units[alias] = unit

    def get_unit(self, name: str) -> BaseUnit:
        """ Get a unit by name, symbol, or alias.
            Raises InvalidUnitError if the name is undefined.
        """
        try:
            return self.units[name]
        except KeyError:
            raise InvalidUnitError(name)

    def parse_unit(self, name: str | BaseUnit) -> BaseUnit:
        """ Parse a unit name into a unit instance.

        Parameters
        ----------
        name : str
            A unit name or composite unit name (i.e "J/kg")

        Returns
        -------
        BaseUnit
            The unit instance.
        """

        # Check if we already have a unit
        if isinstance(name, BaseUnit):
            return name

        if not name or not isinstance(name, str):
            raise TypeError(f"{name!r} is not a valid unit name")

        simple_name = self._simplify_unit(name)

        # Check if the unit is in the registry
        try:
            return self.get_unit(simple_name)
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

    def _parse_unit_name(self, name: str) -> BaseUnit:
        """ Parse a unit string with potential exponent into a unit instance. """
        name, exponent = self._split_exponent(name)
        unit = self.get_unit(name)

        if exponent == 1:
            return unit

        return unit ** exponent

    def _multiply_units(self, name: str) -> BaseUnit:
        """ Parse a unit string with multiplication symbol into a composite unit. """
        units = None
        for name in name.split("*"):
            unit = self._parse_unit_name(name)

            # Check for temperature units which can't be composited
            if unit.dimension.name == "temperature" and not unit.name.endswith("kelvin"):
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

    def _load_units(self) -> None:
        """ Load pre-defined units. """

        path = Path("data")
        alias_file = path / "aliases.json"

        files = list(path.rglob("*.json"))
        files.remove(alias_file)

        if not files:
            raise ConverterError(f"No unit files found in '{path.absolute()}'")

        units = {}

        # Load units
        for filename in files:
            if filename == alias_file:
                continue
            data = self._parse_json(filename)

            # Remove dimension from the rest of the data
            try:
                dimension = data.pop("dimension")
                data.pop("category")  # unused for now
            except KeyError as key:
                raise ConverterError(f"{filename} is missing required {key}")

            # Convert json dictionary to units
            for name, args in data.items():
                if name in units:
                    raise ConverterError(f"{name} is already defined by {units[name]}")

                # The conversion factor is required
                try:
                    factor = args["factor"]
                except KeyError:
                    raise ConverterError(f"{name} is missing required factor")

                # Other keys are optional
                symbols = args.get("symbols", [])
                aliases = args.get("aliases", [])
                prefix = args.get("prefix", None)

                # Add the unit
                self.add_unit(Unit(name, symbols, aliases, dimension, factor, prefix))

        # Load additional unit aliases
        aliases = self._parse_json(alias_file, "aliases")
        for name, unit in aliases.items():
            self.add_alias(name, unit)

    def _parse_json(self, filename: Path, filetype: str = "units") -> dict:
        """ Helper function to parse the specified json file. """
        try:
            with open(filename, "r", encoding="utf-8") as fp:
                return json.load(fp, parse_float=Fraction)

        except OSError as e:
            raise ConverterError(f"Failed to load {filetype} from {filename}",
                                 e.strerror) from None

        except json.JSONDecodeError as e:
            raise ConverterError(f"Invalid json syntax in {filename}",
                                 f"{e.msg}: line {e.lineno} column {e.colno}") from None

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
