# Copyright (c) 2022-2025 Mike Cunningham


import logging

from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.formatting import parse_decimal, simplify_unit, split_exponent
from unitconverter.registry import Registry
from unitconverter.unit import Unit


# Set decimal precision
getcontext().prec = 15


class UnitConverter:

    def __init__(self) -> None:
        """ Initialize unit registry. """
        self.registry = Registry()

    def convert(self, value: Decimal | int | str, source: Unit | str, dest: Unit | str) -> Decimal:
        """ Convert value from source unit to destination unit. """
        value = parse_decimal(value)
        source = self.parse_unit(source)
        dest = self.parse_unit(dest)

        source_categories = self.registry.get_categories(source)
        dest_categories = self.registry.get_categories(dest)

        if source_categories != dest_categories:
            # TODO: solve ambiguity caused by multiple categories by comparing units further
            raise CategoryError(f"Category mismatch: {source} ({", ".join(source_categories)})"
                                f" and {dest} ({", ".join(dest_categories)})")

        # Temperature conversion
        if source_categories == ("temperature",):
            return self._convert_temperature(value, source, dest)

        # Regular conversion
        value = value * source.factor
        return value / dest.factor

    def _convert_temperature(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert between temperature units. """
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
            raise UnitError(f"Invalid temperature unit: {source.name}")

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
            raise UnitError(f"Invalid temperature unit: {dest.name}")

    def compatible_units(self, source: Unit, dest: Unit) -> bool:
        """ Returns True if the units are compatible. For now just compare dimensions. """
        return source.dimen == dest.dimen

    def parse_unit(self, name: Unit | str) -> Unit:
        """ Parse unit string and return a Unit object. """

        # Check if we already have a unit
        if isinstance(name, Unit):
            return name

        # Try to parse the string and find a matching unit
        try:
            return self._parse_unit_name(name)
        except UnitError:
            pass

        # Try to create a composite unit
        return self._parse_composite_unit(name)

    def _parse_unit_name(self, name: str) -> Unit:
        """ Parse a unit name into a Unit instance. """
        # Check if a simplified name is in the registry
        try:
            return self.registry.get_unit(simplify_unit(name))
        except UnitError:
            pass

        # Check if name contains a mathematical expression (not valid here)
        if "*" in name or "/" in name:
            raise UnitError(f"Invalid unit: {name}")

        # Finally, try to split the unit name and exponent
        try:
            return self.registry.get_unit(*split_exponent(name))
        except UnitError:
            raise UnitError(f"{name} is not a valid unit")

    def _parse_composite_unit(self, name: str) -> Unit:
        """ Parse a unit name into a composite Unit instance. """
        # Try to create a composite unit
        names = name.split("/")
        if len(names) == 1:
            numerators = self._parse_names(names[0])
            denominators = []
        elif len(names) == 2:
            numerators = self._parse_names(names[0])
            denominators = self._parse_names(names[1])
        else:
            raise UnitError(f"Invalid unit: {name} - This script only supports one"
                            " division per expression (this feature still in development)")

        numerators = [self._parse_unit_name(numer) for numer in numerators]
        denominators = [self._parse_unit_name(denom) for denom in denominators]

        logging.debug("parse_unit()")
        logging.debug(f"numerators: {numerators}")
        logging.debug(f"denominators: {denominators}")

        # Can't divide units from the same categories for now (i.e metre / inch)
        if len(numerators) == len(denominators) == 1:
            if numerators[0].dimen == denominators[0].dimen:
                category = numerators[0].dimension
                raise UnitError(f"Invalid unit: {name} ({category}/{category})")

        # Celsius, Fahrenheit, and Rankine can't be composited for now
        for unit in numerators + denominators:
            if unit.name in ("celsius", "fahrenheit", "rankine"):
                raise UnitError(f"Invalid unit: {name} - {unit.name} cannot be composited"
                                " (only kelvin is supported for now)")

        # Reduce list of numerators into a single unit
        numer = Unit()
        for unit in numerators:
            numer *= unit

        # Reduce list of denominators into a single unit
        denom = Unit()
        for unit in denominators:
            denom *= unit

        # Try to create the unit
        unit = numer / denom

        logging.debug(f"numer: {numer} ({numer.dimension})")
        logging.debug(f"denom: {denom} ({denom.dimension})")
        logging.debug(f"unit : {unit} ({unit.dimension})")

        if not unit:
            raise UnitError(f"Invalid unit: {name}")

        return unit

    def _parse_names(self, names: str) -> list[str]:
        """ Split numerators or denominators into a list of unit names. """
        return names.split("*")
