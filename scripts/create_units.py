#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import json


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


def create_units(name: str, symbol: str, aliases: list[str] = None) -> dict:
    """ Create a dictionary of metric units. """
    units = {}
    for row in METRIC_TABLE:
        metric_scale, metric_symbol, metric_name = row

        unit_aliases = []
        for alias in aliases:
            unit_aliases.append(metric_name + alias)
        unit_aliases.append(metric_symbol + symbol)

        units[metric_name + name] = {
            'scale': metric_scale,
            'aliases': unit_aliases
        }
    return units


def save_file(units: dict, filename: str, indent=2) -> None:
    """ Save dictionary to json file. """
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(units, outfile, indent=indent)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name',
        help='unit name')

    parser.add_argument(
        'symbol',
        help='unit symbol')

    parser.add_argument(
        'aliases',
        help='optional list of aliases or shortforms',
        nargs='*')

    parser.add_argument(
        '-i', '--indent',
        help='specify a json indent level (default: %(default)s)',
        default=2,
        type=int)

    parser.add_argument(
        '-f', '--filename',
        help='json target file (default: use unit name)',
        default=None)

    args = parser.parse_args()

    if not args.filename:
        args.filename = args.name + '.json'

    units = create_units(args.name, args.symbol, args.aliases)

    save_file(units, args.filename, args.indent)
    print(f'Saved {len(units)} {args.name} units to {args.filename}')
