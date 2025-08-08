# Copyright (c) 2022-2025 Mike Cunningham


import logging
from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.formatting import parse_decimal, simplify_unit, split_exponent
from unitconverter.parsers import load_dimensions, load_units
from unitconverter.models.categories import Categories
from unitconverter.models.registry import Registry
from unitconverter.models.unit import Unit


# Set decimal precision
getcontext().prec = 15


class UnitConverter:

    def __init__(self) -> None:
        """ Initialize pre-defined dimensions and units. """
        self._categories = Categories(load_dimensions())
        self._registry = Registry(load_units())

    def convert(self, value: Decimal | int | str, source: Unit | str, dest: Unit | str) -> Decimal:
        """ Convert value from source unit to destination unit. """
        value = parse_decimal(value)
        source = self.parse_unit(source)
        dest = self.parse_unit(dest)

        # Get category names matching the units dimensions
        source_category = self._categories.get_category(source.dimen)
        dest_category = self._categories.get_category(dest.dimen)

        # NOTE: Extra debugging info. This will will be removed at a future date
        logging.debug(f"{source_category=}")
        logging.debug(f"{dest_category=}")

        # Make sure the units are compatible
        if source_category != dest_category:
            raise CategoryError(source.name, source_category, dest.name, dest_category)

        # Temperature conversion
        if source_category == "temperature":
            return self._convert_temperature(value, source, dest)

        # Regular conversion
        value = value * source.factor
        return value / dest.factor

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
            raise UnitError(f"{source.name} is not a temperature unit")

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
            raise UnitError(f"{dest.name} is not a temperature unit")

    def _parse_unit_name(self, name: str) -> Unit:
        """ Parse a unit name into a Unit instance. """
        # Check if a simplified name is in the registry
        try:
            return self._registry.get_unit(simplify_unit(name))
        except UnitError:
            pass

        # Check if name contains a mathematical expression (not valid here)
        if "*" in name or "/" in name:
            raise UnitError(f"{name} is not a valid unit")

        # Finally, try to split the unit name and exponent
        try:
            return self._registry.get_unit(*split_exponent(name))
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
            raise UnitError(f"{name} is not a valid unit (only one division"
                            " per expression is currently supported)")

        numerators = [self._parse_unit_name(numer) for numer in numerators]
        denominators = [self._parse_unit_name(denom) for denom in denominators]

        logging.debug("parse_unit()")
        logging.debug(f"numerators: {numerators}")
        logging.debug(f"denominators: {denominators}")

        # Can't divide units from the same categories (i.e metre / inch)
        # For now anyway, this might change in the future
        if len(numerators) == len(denominators) == 1:
            if numerators[0].dimen == denominators[0].dimen:
                if numerators != denominators:
                    msg = f"{name} is not a valid unit (cannot divide units in the same category)"
                else:
                    msg = f"{name} is not a valid unit"
                raise UnitError(msg)

        # Celsius, Fahrenheit, and Rankine can't be composited for now
        for unit in numerators + denominators:
            if unit.name in ("celsius", "fahrenheit", "rankine"):
                raise UnitError(f"{unit.name} cannot be composited (only kelvin"
                                " is currently supported)")

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

        logging.debug(f"numer: {numer} ({numer.dimen})")
        logging.debug(f"denom: {denom} ({denom.dimen})")
        logging.debug(f"unit : {unit} ({unit.dimen})")

        if not unit:
            raise UnitError(f"{name} is not a valid unit")

        return unit

    def _parse_names(self, names: str) -> list[str]:
        """ Split numerators or denominators into a list of unit names. """
        return names.split("*")
