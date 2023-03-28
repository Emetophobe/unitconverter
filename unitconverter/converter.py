# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.locale import Locale
from unitconverter.unit import Unit
from unitconverter.units import Units
from unitconverter.prefixes import get_prefixes
from unitconverter.exceptions import UnitError, CategoryError


class Converter:
    """ A basic unit converter. """

    def __init__(self, locale: Locale = Locale.ENGLISH) -> None:
        """ Initialize units. """
        self.units = Units(locale)

    def convert(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert a number from source unit to dest unit.

        Args:
            value (Decimal): the decimal number to convert.
            source (Unit): the source unit.
            dest (Unit): the destination unit.


        Raises:
            ValueError: if the source or dest unit is invalid.

        Returns:
            Decimal: the result of the conversion.
        """

        value = Decimal(value)
        source = self.parse_unit(source)
        dest = self.parse_unit(dest)

        if source.category != dest.category:
            raise CategoryError(source, dest)

        value = source.offset + value * source.factor
        return (-dest.offset + value) / dest.factor

    def parse_unit(self, name: str) -> Unit:
        """ Parse a string and get a Unit.

        Args:
            name (str): unit name, symbol, or alias.

        Raises:
            UnitError: if name is invalid.

        Returns:
            Unit: a unit instance.
        """
        if isinstance(name, Unit):
            return name

        # Check if the unit is in the list
        for unit in self.units:
            if name in unit:
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

        # Invalid unit name
        raise UnitError(name)


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


# TODO: unused for now, find a use or remove
def apply_prefix(prefix: str, unit: Unit) -> Unit:
    """ Apply prefix to a unit and return a new unit.

    Args:
        prefix (str): The prefix name or symbol.
        unit (Unit): the base unit.

    Raises:
        ValueError: if an argument is invalid.

    Returns:
        Unit: a new prefixed unit.
    """
    # Get prefix table from unit scaling option
    prefixes = get_prefixes(unit.prefix_scaling)
    if not prefixes:
        raise ValueError(f'Unit {unit.name!r} does not support prefix scaling.')

    # Create a new unit from prefix
    for factor, symbol, name in prefixes:
        if prefix in (symbol, name):
            return unit.add_prefix(factor, symbol, name)

    raise ValueError(f'Unit {unit.name!r} does not support prefix {prefix!r}.')
