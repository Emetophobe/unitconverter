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
    """ Parse unit files into a unit registry. """

    def create_registry(self) -> Registry:
        """ Create a registry from pre-defined unit files. """
        registry = Registry()

        path = Path("data")
        alias_file = path / "aliases.json"

        files = list(path.glob("*.json"))

        if not files:
            raise ConverterError(f"No unit files found in '{path.absolute()}'")

        units = {}

        # Load units
        for filename in files:
            # Parse alias file separately after all units have been loaded
            if filename == alias_file:
                continue

            data = self._parse_json(filename)

            # Remove dimension from the rest of the data
            try:
                dimension = data.pop("dimension")
            except KeyError:
                raise ConverterError(f"{filename} is missing required dimension")

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
                registry.add_unit(Unit(name, symbols, aliases, dimension, factor, prefix))

        # Load additional unit aliases
        aliases = self._parse_json(alias_file)
        parser = UnitParser(registry)

        for alias, name in aliases.items():
            unit = parser.parse_unit(name)
            registry.add_alias(alias, unit)

        return registry

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
