# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import json

from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import ConverterError
from unitconverter.models.unit import Unit


def load_units() -> dict[str, Unit]:
    """ Load pre-defined units.

    Returns
    -------
    dict[str, Unit]
        A dictionary of unit names and unit objects.

    Raises
    ------
    ConverterError
        If there was an error reading one of the files.
    """

    path = Path("data")
    files = path.rglob("*.json")

    if not files:
        raise ConverterError(f"{path} is missing pre-defined unit files")

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

        # Remove dimension from the rest of the data
        try:
            dimension = data.pop("dimension")
        except KeyError:
            raise ConverterError(f"{filename} is missing required dimension")

        # Remove category from the rest of the data
        try:
            data.pop("category")
        except KeyError:
            raise ConverterError(f"{filename} is missing required category")

        # Convert json dictionary to units
        for name, args in data.items():
            if name in units:
                raise ConverterError(f"{name} is already defined by {units[name]}")

            # The conversion factor is required
            try:
                factor = args["factor"]
            except KeyError:
                raise ConverterError(f"{name} is missing a conversion factor ({filename})")

            # Other keys are optional
            symbols = args.get("symbols", [])
            aliases = args.get("aliases", [])
            prefix = args.get("prefix", None)

            # Create the unit
            units[name] = Unit(name, symbols, aliases, dimension, factor, prefix)

    return units
