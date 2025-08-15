# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import json

from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import ConverterError
from unitconverter.models.dimension import Dimension
from unitconverter.models.unit import Unit


def load_units() -> tuple[dict[str, Dimension], dict[str, Unit]]:
    """ Load pre-defined units from data files.

    Raises:
        ConverterError: If there was an error parsing one of the unit files.

    Returns:
        tuple[dict[str, Dimension], dict[str, Unit]]:
            A tuple of the dimension and unit dictionaries.
    """

    path = Path("data")
    files = path.rglob("*.json")

    if not files:
        raise ConverterError(f"{path} is missing pre-defined unit files")

    dimensions = {}
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
            raise ConverterError("Unit file is missing required dimension", str(filename))

        try:
            category = data.pop("category")
        except KeyError:
            raise ConverterError("Unit file is missing required category", str(filename))

        if category in dimensions:
            raise ConverterError(f"{category} is already defined", str(filename))

        # Store dimension label or "category"
        dimensions[category] = Dimension(dimension)

        # Convert json dictionary to unit definitions
        for name, args in data.items():
            if name in units:
                raise ConverterError(f"{name} is already defined by {units[name]}")

            # Factor is required
            try:
                factor = args["factor"]
            except KeyError:
                raise ConverterError(f"{name} is missing a conversion factor", str(filename))

            # Other arguments are optional
            symbols = args.get("symbols", [])
            aliases = args.get("aliases", [])
            prefix = args.get("prefix", None)

            # TODO: validate data here early so we can raise an error with the filename

            # Create the definition
            units[name] = Unit(name, symbols, aliases, category, dimension, factor, prefix)

    return (dimensions, units)
