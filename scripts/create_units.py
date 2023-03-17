#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import json
from decimal import Decimal, DecimalException


METRIC_TABLE = [
    ('1', '', ''),  # base unit
    ('1e-30', 'q', 'quecto'),
    ('1e-27', 'r', 'ronto'),
    ('1e-24', 'y', 'yocto'),
    ('1e-21', 'z', 'zepto'),
    ('1e-18', 'a', 'atto'),
    ('1e-15', 'f', 'femto'),
    ('1e-12', 'p', 'pico'),
    ('1e-9', 'n', 'nano'),
    ('1e-6', 'µ', 'micro'),
    ('1e-3', 'm', 'milli'),
    ('1e-2', 'c', 'centi'),
    ('1e-1', 'd', 'deci'),
    ('1e+1', 'da', 'deca'),
    ('1e+2', 'h', 'hecto'),
    ('1e+3', 'k', 'kilo'),
    ('1e+6', 'M', 'mega'),
    ('1e+9', 'G', 'giga'),
    ('1e+12', 'T', 'tera'),
    ('1e+15', 'P', 'peta'),
    ('1e+18', 'E', 'exa'),
    ('1e+21', 'Z', 'zetta'),
    ('1e+24', 'Y', 'yotta'),
    ('1e+27', 'R', 'ronna'),
    ('1e+30', 'Q', 'quetta'),
]


def create_units(name: str,
                 symbols: list[str],
                 aliases: list[str] = None,
                 factor: Decimal = None
                 ) -> dict:
    """ Create a dictionary of metric units. """
    if not symbols:
        raise ValueError("Error: missing symbol(s)")

    aliases = aliases or []
    factor = Decimal(factor) if factor else Decimal('1')

    units = {}

    for row in METRIC_TABLE:
        metric_scale, metric_symbol, metric_name = row

        unit_aliases = []
        for alias in aliases:
            unit_aliases.append(metric_name + alias)

        for symbol in symbols:
            unit_aliases.append(metric_symbol + symbol)

        units[metric_name + name] = {
            'scale': Decimal(metric_scale) * factor,
            'aliases': unit_aliases
        }
    return units


def update_units(source: str,
                 name: str,
                 symbols: list[str],
                 aliases: list[str] = None,
                 factor: Decimal = None,
                 indent: int = 2
                 ) -> None:
    """ Update an existing unit table with new metric units. """
    with open(source, 'r', encoding='utf-8') as infile:
        units = json.load(infile)

    units.update(create_units(name, symbols, aliases, factor))
    return units


def save_file(units: dict, filename: str, indent=2) -> None:
    """ Save dictionary to json file. """
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Decimal):
                return str(o)
            return super(DecimalEncoder, self).default(o)

    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(units, outfile, indent=indent, cls=DecimalEncoder)

    print(f'Saved {len(units)} units to {filename}')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name',
        help='unit name')

    parser.add_argument(
        '-s', '--symbols',
        help='list of unit symbols',
        nargs='+')

    parser.add_argument(
        '-a', '--aliases',
        help='list of unit aliases',
        nargs='*')

    parser.add_argument(
        '-f', '--factor',
        help='multiply metric table by a decimal factor (default: %(default)s)',
        default=None)

    parser.add_argument(
        '-i', '--indent',
        help='specify a json indent level (default: %(default)s)',
        default=2,
        type=int)

    parser.add_argument(
        '-u', '--update',
        help='update an existing json file',
        default=None)

    parser.add_argument(
        '-o', '--output',
        help='output file (default: generate filename based on unit name)',
        default=None)

    args = parser.parse_args()

    try:
        if args.update:
            units = update_units(args.update, args.name, args.symbols, args.aliases,
                                 args.factor)
        else:
            units = create_units(args.name, args.symbols, args.aliases, args.factor)

        if not args.output:
            args.output = args.name + '.json'

        save_file(units, args.output, args.indent)
    except DecimalException:
        print('Error: factor is not a valid decimal')
    except ValueError as e:
        print('Error:', e)
    except OSError as e:
        print(f'{e.strerror}: {e.filename}')
