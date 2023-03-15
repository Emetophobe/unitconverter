# Copyright (c) 2022-2023 Mike Cunningham

import json


METRIC_TABLE = [
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
    ('1e1', 'da', 'deca'),
    ('1', '', ''),  # base unit
    ('1e2', 'h', 'hecto'),
    ('1e3', 'k', 'kilo'),
    ('1e6', 'M', 'mega'),
    ('1e9', 'G', 'giga'),
    ('1e12', 'T', 'tera'),
    ('1e15', 'P', 'peta'),
    ('1e18', 'E', 'exa'),
    ('1e21', 'Z', 'zetta'),
    ('1e24', 'Y', 'yotta'),
    ('1e27', 'R', 'ronna'),
    ('1e30', 'Q', 'quetta'),
]


def create_units(name: str, symbol: str, aliases: list[str]) -> dict:
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


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name',
        help='unit name (i.e: "amperes")')

    parser.add_argument(
        'symbol',
        help='unit symbol (i.e "A")')

    parser.add_argument(
        'aliases',
        help='list of aliases or shortforms (i.e "amps")',
        nargs='*')

    parser.add_argument(
        '-i', '--indent',
        help='specify a json indent level (default: %(default)s)',
        default=2,
        type=int
    )

    parser.add_argument(
        '-f', '--filename',
        help='json target file',
        default='temp_units.json'
    )

    args = parser.parse_args()

    units = create_units(args.name, args.symbol, args.aliases)

    with open(args.filename, 'w', encoding='utf-8') as outfile:
        json.dump(units, outfile, indent=args.indent)

    print(f'Saved {len(units)} {args.name} units to {args.filename}')
