# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import logging
from decimal import Decimal


from unitconverter.exceptions import ConversionError, ConverterError
from unitconverter.models.unit import BaseUnit
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.parsers.fileparser import load_units
from unitconverter.registry import Registry
from unitconverter.utils import parse_decimal


class UnitConverter:

    def __init__(self) -> None:
        """ Initialize pre-defined dimensions and units. """
        self.registry = Registry(load_units())
        self.parser = UnitParser(self.registry)

    def convert(self,
                quantity: Decimal,
                source: str | BaseUnit,
                target: str | BaseUnit
                ) -> Decimal:
        """ Convert a quantity from the source unit to the target unit.

        Parameters
        ----------
        quantity : Decimal
            A quantity or value
        source : str | BaseUnit
            Source unit name or instance
        target : str | BaseUnit
            Target unit name or instance

        Returns
        -------
        Decimal
            The converted quantity

        Raises
        ------
        ConverterError:
            If the quantity could not be parsed
        ConverterError:
            If the units could not be parsed
        ConversionError
            If the units are incompatible
        """

        quantity = parse_decimal(quantity)
        source = self.parser.parse_unit(source)
        target = self.parser.parse_unit(target)

        logging.debug(f"convert() {source} ({source.dimension})")
        logging.debug(f"convert() {target} ({target.dimension})")

        # Check if the units are compatible
        if source.dimension != target.dimension:
            raise ConversionError(source, target)

        # Temperature conversion
        if source.dimension.name == "temperature":
            return self.convert_temperature(quantity, source, target)

        # Regular conversion
        quantity = quantity * source.factor
        return quantity / target.factor

    def convert_temperature(self,
                            quantity: Decimal,
                            source: str | BaseUnit,
                            target: str | BaseUnit
                            ) -> Decimal:
        """ Convert between temperature units. """

        quantity = parse_decimal(quantity)
        source = self.parser.parse_unit(source)
        target = self.parser.parse_unit(target)

        # Convert from source unit to kelvin
        if source.name.endswith("kelvin"):
            quantity = quantity * source.factor
        elif source.name.endswith("celsius"):
            quantity = quantity * source.factor + Decimal("273.15")
        elif source.name.endswith("fahrenheit"):
            quantity = (quantity * source.factor + Decimal("459.67")) * Decimal(5) / Decimal(9)
        elif source.name.endswith("rankine"):
            quantity = quantity * source.factor * Decimal(5) / Decimal(9)
        else:
            raise ConverterError(f"{source} is not a temperature unit")

        # Convert from kelvin to target unit
        if target.name.endswith("kelvin"):
            return quantity / target.factor
        elif target.name.endswith("celsius"):
            return (quantity - Decimal("273.15")) / target.factor
        elif target.name.endswith("fahrenheit"):
            return (quantity * Decimal(9) / Decimal(5) - Decimal("459.67")) / target.factor
        elif target.name.endswith("rankine"):
            return (quantity * Decimal(9) / Decimal(5)) / target.factor
        else:
            raise ConverterError(f"{target} is not a temperature unit")
