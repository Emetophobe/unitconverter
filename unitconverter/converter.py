# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import logging
from decimal import Decimal


from unitconverter.exceptions import CategoryError, ConverterError
from unitconverter.models.unit import UnitType, Unit
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.parsers.fileparser import load_units
from unitconverter.registry import Registry
from unitconverter.utils import parse_decimal


class UnitConverter:

    def __init__(self) -> None:
        """ Initialize pre-defined dimensions and units. """
        self.registry = Registry(*load_units())
        self.parser = UnitParser(self.registry)

    def convert(self, value: Decimal, source: str | UnitType, dest: str | UnitType) -> Decimal:
        """ Convert value from source unit to dest unit. Returns the converted value. """

        value = parse_decimal(value)
        source = self.parser.parse_unit(source)
        dest = self.parser.parse_unit(dest)

        logging.debug(f"convert() - {source}, {source.dimen!r}")
        logging.debug(f"convert() - {dest}, {dest.dimen!r}")

        # Make sure the units are compatible
        if not self.compatible(source, dest):
            raise CategoryError(source, dest)

        # Temperature conversion
        if source.dimen == {"temperature": 1}:
            return self.convert_temperature(value, source, dest)

        # Regular conversion
        value = value * source.factor
        return value / dest.factor

    def convert_temperature(self,
                            value: Decimal,
                            source: str | UnitType,
                            dest: str | UnitType
                            ) -> Decimal:
        """ Convert from one temperature unit to another. """

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

    def compatible(self, source: UnitType, dest: UnitType) -> bool:
        """ Check if the units are compatible. """
        if isinstance(source, Unit) and isinstance(dest, Unit):
            if source.category == dest.category:
                return True

        # TODO: better handling of composite units

        # Just compare dimensions for now
        return source.dimen == dest.dimen
