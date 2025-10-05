# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import logging

from fractions import Fraction

from unitconverter.exceptions import ConverterError, IncompatibleUnitError
from unitconverter.models.unit import BaseUnit
from unitconverter.parsers.fileparser import FileParser
from unitconverter.parsers.unitparser import UnitParser
from unitconverter.registry import Registry
from unitconverter.utils import parse_fraction


class UnitConverter:
    """ The unit converter handles loading, parsing, and converting units."""

    def __init__(self) -> None:
        """ Create a unit converter. """
        self.registry = Registry()
        self.parser = UnitParser(self.registry)
        FileParser().load_units(self.registry)

    def convert(self,
                quantity: Fraction,
                source: str | BaseUnit,
                target: str | BaseUnit
                ) -> Fraction:
        """ Convert quantity from the source unit to the target unit.

        Parameters
        ----------
        quantity : Fraction
            A quantity or value
        source : str | BaseUnit
            Source unit name or instance
        target : str | BaseUnit
            Target unit name or instance

        Returns
        -------
        Fraction
            The converted quantity
        """

        quantity = parse_fraction(quantity)
        source = self.parser.parse_unit(source)
        target = self.parser.parse_unit(target)

        logging.debug(f"convert() {source} ({source.dimension})")
        logging.debug(f"convert() {target} ({target.dimension})")

        # Check if the units are compatible
        if source.dimension != target.dimension:
            raise IncompatibleUnitError(source, target)

        # Temperature conversion
        if source.dimension.name == "temperature":
            return self.convert_temperature(quantity, source, target)

        # Regular conversion
        quantity = quantity * source.factor
        return quantity / target.factor

    def convert_temperature(self,
                            quantity: Fraction,
                            source: str | BaseUnit,
                            target: str | BaseUnit
                            ) -> Fraction:
        """ Convert quantity from the source temperature unit to the target unit. """

        quantity = parse_fraction(quantity)
        source = self.parser.parse_unit(source)
        target = self.parser.parse_unit(target)

        # Convert from source unit to kelvin
        if source.name.endswith("kelvin"):
            quantity = quantity * source.factor
        elif source.name.endswith("celsius"):
            quantity = quantity * source.factor + Fraction("273.15")
        elif source.name.endswith("fahrenheit"):
            quantity = (quantity * source.factor + Fraction("459.67")) * Fraction(5, 9)
        elif source.name.endswith("rankine"):
            quantity = quantity * source.factor * Fraction(5, 9)
        else:
            raise ConverterError(f"{source} is not a temperature unit")

        # Convert from kelvin to target unit
        if target.name.endswith("kelvin"):
            return quantity / target.factor
        elif target.name.endswith("celsius"):
            return (quantity - Fraction("273.15")) / target.factor
        elif target.name.endswith("fahrenheit"):
            return (quantity * Fraction(9, 5) - Fraction("459.67")) / target.factor
        elif target.name.endswith("rankine"):
            return (quantity * Fraction(9, 5)) / target.factor
        else:
            raise ConverterError(f"{target} is not a temperature unit")
