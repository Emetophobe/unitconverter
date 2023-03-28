#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import sys
import argparse
from decimal import Decimal, DecimalException
from unitconverter.converter import Locale, Converter, format_decimal


def print_error(error_msg: str, status: int = 1) -> None:
    """ Print an error message and exit. """
    print(error_msg, file=sys.stderr)
    sys.exit(status)


def main() -> None:
    parser = argparse.ArgumentParser(description='A simple unit converter')

    parser.add_argument(
        'value',
        help='integer or decimal value.')

    parser.add_argument(
        'source',
        help='source unit.')

    parser.add_argument(
        'dest',
        help='destination unit.')

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
        '-a', '--american',
        help='use American spelling instead of British (default: False)',
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

    # Get locale
    locale = Locale.AMERICAN if args.american else Locale.ENGLISH

    # Perform the conversion
    try:
        converter = Converter(locale)
        result = converter.convert(value, args.source, args.dest)
    except DecimalException:
        print_error('Error: Invalid decimal operation')
    except OSError as e:
        print_error(f'Error reading {e.filename} ({e.strerror})')
    except ValueError as e:
        print_error(e)

    # Display result
    value = format_decimal(value, commas=args.commas)
    result = format_decimal(result, args.exponent, args.precision, args.commas)
    print(f'{value} {args.source} = {result} {args.dest}')


if __name__ == '__main__':
    main()
