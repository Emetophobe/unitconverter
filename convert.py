#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import sys
import argparse
import json
from pathlib import Path
from decimal import Decimal, DecimalException


class Converter:
    def __init__(self):
        self.load_units()

    def convert(self, value, source, dest):
        """ Convert a number from source unit to dest unit.

        Args:
            value (Decimal): the decimal number to convert.
            source (str): the source unit name.
            dest (str): the destination unit name.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            ValueError: if the source or dest unit is invalid.
        """
        value = Decimal(value)

        source_category, source_name, source_scale = self.find_unit(source)
        dest_category, dest_name, dest_scale = self.find_unit(dest)

        if source_category != dest_category:
            raise ValueError(f'Error: unit mismatch:'
                             f' {source_name}={source_category},'
                             f' {dest_name}={dest_category}')

        # Temperature is a special case
        if source_category == 'temperature':
            return self.convert_temperature(value, source_name, dest_name)

        source_value = Decimal(source_scale)
        dest_value = Decimal(dest_scale)

        return value * (source_value / dest_value)

    def find_unit(self, name):
        """ Find a unit matching the specified name or alias.

        Args:
            name (str): the name of the unit (i.e "meters").

        Returns:
            tuple[str, str, str]: the unit category, name, and scale.

        Raises:
            ValueError: if name was not found.
        """
        for category, units in self.units.items():
            for unitname, properties in units.items():
                aliases = properties['aliases']
                if name == unitname or name in aliases:
                    scale = properties['scale']
                    return (category, unitname, scale)

        raise ValueError(f'Invalid unit name: {name}')

    def convert_temperature(self, value, source, dest):
        """ Convert temperatures using kelvin as a baseline.

        Args:
            value (Decimal): the decimal value to convert.
            source (str): the source unit name.
            dest (str): the destination unit name.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            ValueError: if the source or dest unit is invalid.
        """
        kelvin = self.to_kelvin(value, source)
        return self.from_kelvin(kelvin, dest)

    def to_kelvin(self, value, source_unit):
        if source_unit == 'celcius':
            return value + Decimal(273.15)
        elif source_unit == 'fahrenheit':
            return (value + Decimal(459.67)) * Decimal(5 / 9)
        elif source_unit == 'rankine':
            return value * Decimal(5 / 9)
        elif source_unit == 'kelvin':
            return value
        else:
            raise ValueError(f'Invalid unit name: {source_unit}')

    def from_kelvin(self, value, dest_unit):
        if dest_unit == 'celcius':
            return value - Decimal(273.15)
        elif dest_unit == 'fahrenheit':
            return value * Decimal(9 / 5) - Decimal(459.67)
        elif dest_unit == 'rankine':
            return value * Decimal(9 / 5)
        elif dest_unit == 'kelvin':
            return value
        else:
            raise ValueError(f'Invalid unit name: {dest_unit}')

    def load_units(self):
        """ Load unit categories from json files. """
        self.units = {}
        for path in Path('./data/').glob('*.json'):
            with open(path, 'r', encoding='utf-8') as infile:
                data = json.load(infile)
                self.units[path.stem] = data

            with open(path, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=2)

    def list_units(self, category=None):
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


def remove_exponent(value):
    if value == value.to_integral():
        return value.quantize(Decimal(1))
    else:
        return value.normalize()


def print_error(error_msg):
    print(error_msg, file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='A basic unit converter.')

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

    # Perform the conversion
    try:
        result = converter.convert(value, args.source, args.dest)
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
