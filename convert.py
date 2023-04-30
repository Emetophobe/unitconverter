#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import argparse
import logging
import sys
from decimal import Decimal, DecimalException

from unitconverter.converter import convert
from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_decimal


def print_error(error_msg: str, status: int = 1) -> None:
    """ Print an error message and exit. """
    print(error_msg, file=sys.stderr)
    sys.exit(status)


def main() -> None:
    parser = argparse.ArgumentParser(description='A simple unit converter')

    parser.add_argument(
        'value',
        help='integer or decimal value')

    parser.add_argument(
        'source',
        help='the source unit')

    parser.add_argument(
        'dest',
        help='one or more destination units',
        nargs='+')

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

    parser.add_argument(
        '-d', '--debug',
        help=argparse.SUPPRESS,
        action='store_true')

    args = parser.parse_args()

    # Check value argument
    try:
        value = Decimal(args.value)
    except DecimalException:
        print_error(f'Error: {args.value} is not a valid number.')

    # Check precision argument
    if args.precision is not None and (args.precision < 0 or args.precision > 20):
        print_error('Error: precision must be between 0 and 20.')

    # Configure debug logger
    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.WARNING)
    logging.basicConfig(format='debugging: %(message)s')

    # Perform the conversion(s)
    try:
        results = [(convert(value, args.source, dest), dest) for dest in args.dest]
    except DecimalException:
        print_error('Error: Invalid decimal operation')
    except ConverterError as e:
        print_error(e)

    value = format_decimal(value, commas=args.commas)
    padding = ' ' * len(f'{value} {args.source}')

    # Display result(s)
    for index, (result, dest) in enumerate(results):
        result = format_decimal(result, args.exponent, args.precision, args.commas)

        if index == 0:
            print(f'{value} {args.source} = {result} {dest}')
        else:
            print(f'{padding} = {result} {dest}')


if __name__ == '__main__':
    main()
