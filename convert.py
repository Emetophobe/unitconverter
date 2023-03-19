#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import sys
import argparse
import json
from pathlib import Path
from decimal import Decimal, DecimalException
from typing import Optional


METRIC_TABLE = [
    ('1', '', ''),  # base unit
    ('1E-30', 'q', 'quecto'),
    ('1E-27', 'r', 'ronto'),
    ('1E-24', 'y', 'yocto'),
    ('1E-21', 'z', 'zepto'),
    ('1E-18', 'a', 'atto'),
    ('1E-15', 'f', 'femto'),
    ('1E-12', 'p', 'pico'),
    ('1E-9', 'n', 'nano'),
    ('1E-6', 'µ', 'micro'),
    ('1E-3', 'm', 'milli'),
    ('1E-2', 'c', 'centi'),
    ('1E-1', 'd', 'deci'),
    ('1E+1', 'da', 'deca'),
    ('1E+2', 'h', 'hecto'),
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]


class Unit:
    """ A single unit of measurement. """

    def __init__(self, name: str, category: str, scale: str, aliases: list[str]) -> None:
        self.name = name
        self.category = category
        self.scale = scale
        self.aliases = aliases

    def __contains__(self, name) -> bool:
        return name == self.name or name in self.aliases

    def __str__(self) -> str:
        return f'{self.scale} {self.name}, {self.category}, {self.aliases}'

    def __repr__(self) -> str:
        return f'Unit({self.name}, {self.category}, {self.scale}, {self.aliases})'


class Converter:
    """ A basic unit converter. """

    def __init__(self) -> None:
        self.load_units()

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

        if source.category == 'temperature':
            # Special case: temperature uses a custom converter
            kelvin = self.to_kelvin(value, source)
            return self.from_kelvin(kelvin, dest)
        else:
            # Perform the conversion normally
            return value * (Decimal(source.scale) / Decimal(dest.scale))

    def to_kelvin(self, value: Decimal, source: Unit) -> Decimal:
        """ Convert temperature unit to kelvin. """
        five_ninths = Decimal('5') / Decimal('9')
        if source.name == 'celsius':
            return value + Decimal('273.15')
        elif source.name == 'fahrenheit':
            return (value + Decimal('459.67')) * five_ninths
        elif source.name == 'rankine':
            return value * five_ninths
        elif source.name.endswith('kelvin'):
            return value * (Decimal(source.scale) / Decimal('1'))
        else:
            raise ValueError(f'Invalid unit name: {source.name}')

    def from_kelvin(self, value: Decimal, dest: Unit) -> Decimal:
        """ Convert temperature unit from kelvin. """
        nine_fifths = Decimal('9') / Decimal('5')
        if dest.name == 'celsius':
            return value - Decimal('273.15')
        elif dest.name == 'fahrenheit':
            return value * nine_fifths - Decimal('459.67')
        elif dest.name == 'rankine':
            return value * nine_fifths
        elif dest.name.endswith('kelvin'):
            return value * (Decimal('1') / Decimal(dest.scale))
        else:
            raise ValueError(f'Invalid unit name: {dest.name}')

    def parse_unit(self, name: str) -> Unit:
        """ Parse a unit string and return a Unit instance.

        Args:
            name (str): unit name, symbol, or alias.

        Raises:
            ValueError: if the unit name is invalid.

        Returns:
            Unit: the unit instance.
        """

        # Check if we can find the unit right away
        if unit:= self.find_unit(name):
            return unit

        # Otherwise check the metric scale for a matching symbol or name.
        for scale, symbol, prefix in METRIC_TABLE[1:]:
            for start in (symbol, prefix):
                if name.startswith(start):
                    if unit := self.find_unit(name.removeprefix(start)):
                        unit.name = prefix + unit.name
                        unit.scale = (Decimal(scale) * Decimal(unit.scale))
                        return unit

        raise ValueError(f'Unit not found: {name}')

    def find_unit(self, name: str) -> Optional[Unit]:
        """ Find a unit matching the specified name or alias.

        Args:
            name (str): the name of the unit; i.e "meters".

        Returns:
            Unit: the unit instance, or None if not found.
        """
        for category, units in self.units.items():
            for unitname, properties in units.items():
                if name == unitname or name in properties['aliases']:
                    return Unit(unitname, category, **properties)
        return None

    def load_units(self) -> None:
        """ Load unit categories from json files. """
        self.units = {}
        for path in Path('./data/').glob('*.json'):
            with open(path, 'r', encoding='utf-8') as infile:
                data = json.load(infile)
                category = path.stem.replace('_', ' ')
                self.units[category] = data


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int = None,
                   commas: bool = False,
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


def print_error(error_msg: str, status: int = 1) -> None:
    """ Print an error message and exit.

    Args:
        error_msg (str): the error message.
        status (int, optional): the exit code. Defaults to 1.
    """
    print(error_msg, file=sys.stderr)
    sys.exit(status)


def main() -> None:
    parser = argparse.ArgumentParser(description='A simple unit converter.')

    parser.add_argument(
        'value',
        help='integer or float value to convert.')

    parser.add_argument(
        'source',
        help='name of the source unit.')

    parser.add_argument(
        'dest',
        help='name of the destination unit.')

    parser.add_argument(
        '-p', '--precision',
        help='set rounding precision (default: %(default)s)',
        metavar='ndigits',
        default=None,
        type=int)

    parser.add_argument(
        '-c', '--commas',
        help='show thousands separator (default: False)',
        action='store_true')

    parser.add_argument(
        '-e', '--exponent',
        help='show E notation when possible (default: False)',
        action='store_true')

    args = parser.parse_args()

    # Load the unit converter
    try:
        converter = Converter()
    except OSError as e:
        print(f'Error reading unit file: {e.filename} ({e.strerror})')

    # Convert user value to a Decimal
    try:
        value = Decimal(args.value)
    except DecimalException:
        print_error(f'Error: {args.value} is not a valid number.')

    # Check precision
    if args.precision is not None and (args.precision < 0 or args.precision > 20):
        print_error('Error: precision must be between 0 and 20.')

    # Get the source and dest units
    try:
        source = converter.parse_unit(args.source)
        dest = converter.parse_unit(args.dest)
    except ValueError as e:
        print_error(e)

    if source.category != dest.category:
        print_error(f'Error: unit mismatch:'
                    f' {source.name}={source.category},'
                    f' {dest.name}={dest.category}')

    # Perform the conversion
    try:
        result = converter.convert(value, source, dest)
    except ValueError as e:
        print_error(e)
    except DecimalException:
        print_error('Error: Invalid decimal operation')

    # Display result
    value = format_decimal(value, commas=args.commas)
    result = format_decimal(result, args.exponent, args.precision, args.commas)
    print(f'{value} {args.source} = {result} {args.dest}')


if __name__ == '__main__':
    main()
