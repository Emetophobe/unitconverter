#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import sys
from collections import defaultdict
from pathlib import Path
from format_json import file_checksum

sys.path.append('.')  # is there a better way?
from unitconverter.registry import get_units # noqa


DEST_FILE = Path('docs/supported_units.txt')


def create_supported_units(filename):
    """ Generate a text file of all supported units. """
    categories = get_categories(get_units())
    sorted_categories = sorted(categories.keys())

    old_checksum = file_checksum(filename)
    total_units = 0

    with open(filename, 'w', encoding='utf-8') as outfile:
        for category in sorted_categories:
            outfile.write('\n')

            units = categories[category]
            total_units += len(units)

            outfile.write(format_name(category.title()) + '\n\n')
            for unit in units:
                outfile.write('\t' + format_name(unit.name) + '\n')

    new_checksum = file_checksum(filename)
    if old_checksum != new_checksum:
        print(f'Saved {total_units} units to {DEST_FILE}')
    else:
        print(f'{filename.name} is already up to date.')


def get_categories(units: dict) -> dict:
    """ Convert units dict to a dictionary of categories and units. """
    categories = defaultdict(list)
    for unit in units.values():
        if not unit.is_prefixed:
            categories[unit.category].append(unit)
    return categories


replace_powers = {
    '2': '²',
    '3': '³',
}


def format_name(name: str) -> str:
    #  if '/' in name:
    #    name = name.replace('/', ' per ')

    for key, value in replace_powers.items():
        if name.endswith(key):
            return name[:-1] + value

    return name


if __name__ == '__main__':
    create_supported_units(DEST_FILE)
