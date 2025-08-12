# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError, ConverterError
from unitconverter.formatting import parse_decimal
from unitconverter.models.unit import Unit
from unitconverter.parsers.fileparser import load_units
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.registry import Registry


# Set decimal precision
getcontext().prec = 15


class UnitConverter:

    def __init__(self) -> None:
        """ Initialize pre-defined dimensions and units. """
        self.registry = Registry(*load_units())
        self.parser = UnitParser(self.registry)

    def convert(self, value: Decimal | int | str, source: Unit | str, dest: Unit | str) -> Decimal:
        """ Convert a value from the source unit to the destination unit.

        Args:
            value (Decimal | int | str): The value to convert.
            source (Unit | str): A unit name or unit instance.
            dest (Unit | str): A unit name or unit instance.

        Raises:
            CategoryError: If the unit categories are incompatible.
            ConverterError: If an argument is invalid.

        Returns:
            Decimal: The conversion result.
        """
        value = parse_decimal(value)
        source = self.parser.parse_unit(source)
        dest = self.parser.parse_unit(dest)

        # Get the unit categories
        source_category = self.registry.get_category(source)
        dest_category = self.registry.get_category(dest)

        # Compare unit dimensions if a unit has no pre-defined category
        if source_category is None or dest_category is None:
            if source.dimen != dest.dimen:
                raise CategoryError(source.name, str(source.dimen), dest.name, str(dest.dimen))

        # Compare unit categories
        elif source_category != dest_category:
            raise CategoryError(source.name, source_category, dest.name, dest_category)

        # Temperature conversion
        if source_category == "temperature":
            return self.convert_temperature(value, source, dest)

        # Regular conversion
        value = value * source.factor
        return value / dest.factor

    def convert_temperature(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert between temperature units.

        Args:
            value (Decimal | int | str): The value to convert.
            source (Unit | str): The source unit.
            dest (Unit | str): The destination unit.

        Raises:
            ConverterError: If a unit is not a valid temperature unit.

        Returns:
            Decimal: The conversion result.
        """
        value = parse_decimal(value)
        source = self.parser.parse_unit(source)
        dest = self.parser.parse_unit(dest)

        # Convert from source to kelvin
        if source.name.endswith("kelvin"):
            value = value * source.factor
        elif source.name == "celsius":
            value = value + Decimal("273.15")
        elif source.name == "fahrenheit":
            value = (value + Decimal("459.67")) * Decimal(5) / Decimal(9)
        elif source.name == "rankine":
            value = value * Decimal(5) / Decimal(9)
        else:
            raise ConverterError(f"{source} is not a temperature unit")

        # Convert from kelvin to dest
        if dest.name.endswith("kelvin"):
            return value / dest.factor
        elif dest.name == "celsius":
            return value - Decimal("273.15")
        elif dest.name == "fahrenheit":
            return value * Decimal(9) / Decimal(5) - Decimal("459.67")
        elif dest.name == "rankine":
            return value * Decimal(9) / Decimal(5)
        else:
            raise ConverterError(f"{dest} is not a temperature unit")
