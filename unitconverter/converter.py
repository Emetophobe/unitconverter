# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.prefixes import get_prefixes
from unitconverter.unit import Unit
from unitconverter.units import Units
from unitconverter.utils import parse_decimal, simplify_unit


class Converter:
    """ A basic unit converter. """

    def __init__(self) -> None:
        """ Initialize units. """
        self.units = Units()

    def convert(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert a number from source unit to dest unit.

        Args:
            value (Decimal): a decimal, int, or str value.
            source (Unit): a source unit.
            dest (Unit): a destination unit.

        Raises:
            UnitError: if a unit is invalid.
            CategoryError: if the units are incompatible.

        Returns:
            Decimal: the result of the conversion.
        """

        value = parse_decimal(value)
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
            UnitError: if the unit name is invalid.

        Returns:
            Unit: a unit instance.
        """
        if isinstance(name, Unit):
            return name

        # Get simplified unit name
        simple_name = simplify_unit(name)

        # Check pre-defined list for a matching unit
        for unit in self.units:
            if simple_name in unit:
                return unit

        # Check generated prefixes for a matching unit
        for unit in self.units:
            # Get prefix table based on unit prefix option
            prefixes = get_prefixes(unit.prefix_scale)

            # Generate prefixes and check for a matching unit
            for factor, symbol, prefix in prefixes:
                prefix_unit = unit.scale(factor, symbol, prefix)
                if simple_name in prefix_unit:
                    return prefix_unit

        # Invalid unit name
        raise UnitError(f'Invalid unit: {name}')


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
