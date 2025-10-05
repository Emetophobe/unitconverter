# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import json

from fractions import Fraction
from pathlib import Path

from unitconverter.exceptions import ConverterError
from unitconverter.models.unit import Unit
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.registry import Registry


class FileParser:
    """ Load unit definitions into a unit registry. """

    def load_units(self, registry: Registry) -> None:
        """ Load pre-defined units into the specified registry. Clears existing units. """

        if not isinstance(registry, Registry):
            raise TypeError(f"{registry!r} is not a valid unit registry")

        path = Path("data")

        files = list(path.glob("*.json"))
        alias_file = path / "aliases.json"

        # Remove aliases from the rest of the files
        try:
            files.remove(alias_file)
        except ValueError:
            raise ConverterError("missing required aliases.json file")

        if not files:
            raise ConverterError(f"No unit files found in '{path.absolute()}'")

        # Clear existing units to avoid duplicates
        registry.clear()

        # Load unit files
        for filename in files:
            data = self._parse_json(filename)

            # Get dimension from the top of the unit file
            dimension = data.pop("dimension", None)
            if dimension is None:
                raise ConverterError(f"{filename} is missing required dimension")

            # Convert unit dictionary to unit instances
            for name, args in data.items():
                # The conversion factor is required
                factor = args.get("factor", None)
                if factor is None:
                    raise ConverterError(f"{name} is missing required factor")

                # Other keys are optional
                symbols = args.get("symbols", [])
                aliases = args.get("aliases", [])
                prefixes = args.get("prefix", None)

                # Create the unit
                registry.add_unit(Unit(name, symbols, aliases, dimension, factor, prefixes))

        # Load composite unit aliases
        aliases = self._parse_json(alias_file)
        parser = UnitParser(registry)

        for alias, name in aliases.items():
            unit = parser.parse_unit(name)
            registry.add_alias(alias, unit)

    def _parse_json(self, filename: Path) -> dict:
        """ Parse a json file into a dictionary. """
        try:
            with open(filename, "r", encoding="utf-8") as fp:
                return json.load(fp, parse_float=Fraction)

        except OSError as e:
            raise ConverterError(f"Failed to load units from {filename}", e.strerror)

        except json.JSONDecodeError as e:
            raise ConverterError(f"Invalid json syntax in {filename}",
                                 f"{e.msg}: line {e.lineno} column {e.colno}")
