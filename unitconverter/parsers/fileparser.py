# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import json

from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import ConverterError
from unitconverter.models.definition import Definition
from unitconverter.models.dimension import Dimension


def load_units() -> tuple[dict[str, Dimension], dict[str, Definition]]:
    """ Load pre-defined dimensions and units from json files.

    Raises:
        ConverterError: If there was an error parsing one of the unit files.

    Returns:
        tuple[dict[str, Dimension], dict[str, Definition]]:
            A tuple of the dimensions and unit definitions.
    """

    path = Path("data")
    files = path.rglob("*.json")

    if not files:
        raise ConverterError(f"{path} is missing pre-defined unit files")

    categories = {}
    units = {}

    for filename in files:
        # Load each unit file individually
        try:
            with open(filename, "rb") as fp:
                data = json.load(fp, parse_float=Decimal)
        except OSError as e:
            raise ConverterError(f"Failed to load units from {e.filename} ({e.strerror})")
        except json.JSONDecodeError as e:
            raise ConverterError(f"Invalid json syntax in {filename} - {e}")

        try:
            dimension = data.pop("dimension")
        except KeyError:
            raise ConverterError("Unit file is missing required dimension", filename)

        try:
            category = data.pop("category")
        except KeyError:
            raise ConverterError("Unit file is missing required category", filename)

        if category in categories:
            raise ConverterError(f"{category} is already defined")
        else:
            categories[category] = Dimension(dimension)

        # Convert json dictionary to unit definitions
        for name, args in data.items():
            if name in units:
                raise ConverterError(f"{name} is already defined")

            # Required argument
            try:
                factor = args["factor"]
            except KeyError:
                raise ConverterError(f"{name} is missing a conversion factor", filename)

            # Optional arguments
            symbols = args.get("symbols", [])
            aliases = args.get("aliases", [])
            prefix = args.get("prefix", None)

            # Create the definition
            units[name] = Definition(name, symbols, aliases, factor, category, dimension, prefix)

    return (categories, units)
