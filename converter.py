#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import sys
import argparse
import json
from pathlib import Path
from decimal import Decimal, DecimalException


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

        # Temperature is a special case
        if source.category == 'temperature':
            return self.convert_temperature(value, source, dest)
        else:
            return value * (Decimal(source.scale) / Decimal(dest.scale))

    def convert_temperature(self, value: Decimal, source: Unit, dest: Unit) -> Decimal:
        """ Convert temperatures using kelvin as a baseline.

        Args:
            value (Decimal): the decimal value to convert.
            source (Unit): the source unit.
            dest (Unit): the destination unit.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            ValueError: if the source or dest unit is invalid.
        """
        kelvin = self.to_kelvin(value, source)
        return self.from_kelvin(kelvin, dest)

    def to_kelvin(self, value: Decimal, source: Unit) -> Decimal:
        """ Convert temperature unit to kelvin. """
        five_ninths = Decimal('5') / Decimal('9')
        if source.name == 'celsius':
            return value + Decimal('273.15')
        elif source.name == 'fahrenheit':
            return (value + Decimal('459.67')) * five_ninths
        elif source.name == 'rankine':
            return value * five_ninths
        elif source.name == 'kelvin':
            return value
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
        elif dest.name == 'kelvin':
            return value
        else:
            raise ValueError(f'Invalid unit name: {dest.name}')

    def find_unit(self, name: str) -> Unit:
        """ Find a unit matching the specified name or alias.

        Args:
            name (str): the name of the unit (i.e "meters").

        Returns:
            Unit: the unit instance.

        Raises:
            ValueError: if name was not found.
        """
        for category, units in self.units.items():
            for unitname, properties in units.items():
                if name == unitname or name in properties['aliases']:
                    return Unit(unitname, category, **properties)

        raise ValueError(f'Invalid unit name: {name}')

    def load_units(self) -> None:
        """ Load unit categories from json files. """
        self.units = {}
        for path in Path('./data/').glob('*.json'):
            with open(path, 'r', encoding='utf-8') as infile:
                data = json.load(infile)
                self.units[path.stem] = data

    def list_units(self, category: str = None) -> None:
        """ List available units.

        Args:
            category (str, optional): name of the category,
            or None to show all categories. Defaults to None.

        Raises:
            ValueError: if the category name is invalid.
        """
        if category and category not in self.units.keys():
            raise ValueError(f'Invalid category: {category}')

        columns = "{:>20} {:>20}   {}"
        for name, units in self.units.items():
            if not category or name == category:
                print('Category:', name)
                print()
                print(columns.format('scale', 'name', 'aliases or symbols'))
                for unit, properties in units.items():
                    scale = properties['scale']
                    aliases = properties['aliases']
                    print(columns.format(scale, unit, ', '.join(aliases)))
                print()


def remove_exponent(value: Decimal) -> Decimal:
    """ Convert exponent notation to decimal notation if possible.

    Args:
        value (Decimal): source value.

    Returns:
        Decimal: the converted value.
    """
    if value == value.to_integral():
        return value.quantize(Decimal(1))
    else:
        return value.normalize()


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
        help='rounding precision (default: %(default)s)',
        metavar='size',
        default=None,
        type=int)

    parser.add_argument(
        '-c', '--comma',
        help='show thousands separator (default: False)',
        action='store_true'
    )

    parser.add_argument(
        '-l', '--list',
        help='list unit categories and exit',
        action='store_true')

    args = parser.parse_args()

    # Load the unit converter
    try:
        converter = Converter()
    except OSError as e:
        print(f'Error reading unit file: {e.filename} ({e.strerror})')

    if args.list:
        converter.list_units()
        return

    # Convert user value to a Decimal
    try:
        value = Decimal(args.value)
    except DecimalException:
        print_error(f'Error: {args.value} is not a valid number.')

    precision = args.precision
    if precision is not None and (precision < 0 or precision > 20):
        print_error('Error: precision must be between 0 and 20.')

    # Get the source and dest units
    try:
        source = converter.find_unit(args.source)
        dest = converter.find_unit(args.dest)
    except ValueError as e:
        print_error(e)

    if source.category != dest.category:
        print_error(f'Error: unit mismatch:'
                    f' {source.name}={source.category},'
                    f' {dest.name}={dest.category}')

    # Perform the conversion
    try:
        result = converter.convert(value, source, dest)
        result = remove_exponent(result)
    except ValueError as e:
        print_error(e)
    except DecimalException:
        print_error('Error: Invalid decimal operation')

    # Display the result
    commas = ',' if args.comma else ''
    precision = f'.{precision}f' if precision is not None else ''
    print(f'{value:{commas}} {args.source} = {result:{commas}{precision}} {args.dest}')


if __name__ == '__main__':
    main()
