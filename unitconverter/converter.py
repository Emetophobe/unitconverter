# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from typing import Optional
from unitconverter.unit import Unit, get_prefixes
from unitconverter.units import get_units


class Converter:
    """ A basic unit converter. """

    def __init__(self) -> None:
        self.units = get_units()

    def convert(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert a number from source unit to dest unit.

        Args:
            value (Decimal): the decimal number to convert.
            source (Unit): the source unit.
            dest (Unit): the destination unit.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            ValueError: if the source or dest unit is invalid.
        """
        value = Decimal(value)

        if source.category != dest.category:
            raise ValueError(f'Error: unit mismatch:'
                             f' {source.name} ({source.category}),'
                             f' {dest.name} ({dest.category})')

        value = source.offset + value * source.factor
        return (-dest.offset + value) / dest.factor

    def parse_unit(self, name: str) -> Unit:
        """ Parse a unit string and return a Unit instance.

        Args:
            name (str): unit name, symbol, or alias.

        Raises:
            ValueError: if the unit name is invalid.

        Returns:
            Unit: the unit instance.
        """

        # Check if the unit is in the list
        if unit := self.find_unit(name):
            return unit

        # Check supported prefixes for a matching unit
        for unit in self.units:
            # Get prefix table based on unit scaling option
            prefixes = get_prefixes(unit.prefix_scaling)

            # Generate prefixes and check for a matching unit
            for factor, symbol, prefix in prefixes:
                prefix_unit = unit.add_prefix(factor, symbol, prefix)
                if name in prefix_unit:
                    return prefix_unit

        raise ValueError(f'Invalid unit name: {name}')

    def find_unit(self, name: str) -> Optional[Unit]:
        """ Find a unit by name, alias, or symbol.

        Args:
            name (str): the name of the unit; i.e "metres".

        Returns:
            Unit: the unit instance, or None if not found.
        """
        for unit in self.units:
            if name in unit:
                return unit
        return None


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int = None,
                   commas: bool = False
                   ) -> str:
    """ Format a decimal into a string for display.

    Args:
        value (Decimal): the decimal value.
        exponent (bool, optional): use e notation when possible. Defaults to False.
        precision (int, optional): set rounding precision. Defaults to None.
        commas (bool, optional): use commas for thousands separators. Defaults to False.

    Returns:
        str: the formatted string.
    """
    precision = f'.{precision}' if precision is not None else ''

    if exponent:
        return f'{value:{precision}E}'

    comma = ',' if commas else ''
    return f'{value:{comma}{precision}f}'
