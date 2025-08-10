# Copyright (c) 2022-2025 Mike Cunningham


import tomllib

from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import ConverterError
from unitconverter.models.definition import Definition
from unitconverter.models.dimension import Dimension


def load_dimensions() -> dict[str, Dimension]:
    """ Load pre-defined dimensions from file.

    Raises:
        ConverterError: If the dimensions file could not be read.

    Returns:
        dict[str, Dimension]: A dictionary of category names and their dimensions.
    """
    try:
        with open("data/dimensions.toml", "rb") as fp:
            # TODO: parse and validate the dictionary here
            return tomllib.load(fp, parse_float=Decimal)
    except OSError as e:
        raise ConverterError(f"Failed to load dimensions from {e.filename} ({e.strerror})")


def load_units() -> dict[str, Definition]:
    """ Load pre-defined units from unit files.

    Raises:
        ConverterError: If there was an error parsing a unit file.

    Returns:
        dict[str, Definition]: A dictionary of unit names and unit definitions.
    """

    path = Path("data/units")
    files = path.rglob("*.toml")

    if not files:
        raise ConverterError(f"Missing pre-defined unit files in {path}")

    units = {}

    for filename in files:
        # Load each unit file individually
        try:
            with open(filename, "rb") as fp:
                data = tomllib.load(fp, parse_float=Decimal)
        except OSError as e:
            raise ConverterError(f"Failed to load units from {e.filename} ({e.strerror})")

        # Just use the filename as the category name for now
        # In the future the category should be part of the file data
        category = filename.stem.replace("_", " ")

        # Make sure to pop dimension to separate it from the unit data
        try:
            dimensions = data.pop("dimension")
        except KeyError:
            raise ConverterError("Unit file is missing required dimension", filename)

        # Convert toml dictionary into a dictionary of unit definitions
        for name, args in data.items():
            if name in units:
                raise ConverterError(f"{name} is already defined (unit names must be unique)")

            # Required arguments
            try:
                factor = args["factor"]
            except KeyError:
                raise ConverterError(f"{name} is missing a conversion factor", filename)

            # Optional arguments
            symbols = args.get("symbols", [])
            aliases = args.get("aliases", [])
            prefix = args.get("prefix", None)

            # Create the unit definition
            units[name] = Definition(name, symbols, aliases, factor, category, dimensions, prefix)

    return units
