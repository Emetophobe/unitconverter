#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham


import sys
import argparse
import decimal
from src import get_converter, find_unit


def main():
    parser = argparse.ArgumentParser(description='A basic unit converter.')

    parser.add_argument(
        'number',
        help='integer or float to convert.')

    parser.add_argument(
        'source',
        help='name of the source unit.')

    parser.add_argument(
        'dest',
        help='name of the destination unit.')

    parser.add_argument(
        '-p', '--precision',
        help='decimal precision (default: %(default)s)',
        default=5,
        type=int)

    args = parser.parse_args()

    try:
        source_category, source = find_unit(args.source)
        dest_category, dest = find_unit(args.dest)
    except ValueError as e:
        raise SystemExit(e)

    if source_category != dest_category:
        raise SystemExit(f'Unit mismatch: {args.source}={source_category},'
                         f' {args.dest}={dest_category}')

    try:
        converter = get_converter(source_category)
    except ValueError as e:
        raise SystemExit(e)

    try:
        number = decimal.Decimal(args.number)
    except decimal.InvalidOperation:
        parser.error(f'{args.number} is not a valid number.')

    if args.precision < 1 or args.precision > 20:
        parser.error('precision must be between 1 and 20.')

    decimal.getcontext().prec = args.precision

    try:
        result = converter.convert(number, source, dest)
        print(f'{number} {source} = {result} {dest}')
    except ValueError as e:
        sys.exit(e)
    except KeyError as e:
        sys.exit(f'Invalid unit name: {e}')
    except decimal.InvalidOperation:
        sys.exit('Error: the decimal is too large.')


if __name__ == '__main__':
    main()
