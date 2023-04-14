#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import sys
from pathlib import Path
from format_json import file_checksum

sys.path.append('.')  # is there a better way?
from unitconverter.registry import Registry  # noqa


DEST_FILE = Path('docs/supported_units.txt')


def create_supported_units(filename):
    """ Generate a text file of all supported units. """
    all_units = Registry()
    categories = all_units.get_categories()
    sorted_categories = sorted(categories.keys())

    old_checksum = file_checksum(filename)

    with open(filename, 'w', encoding='utf-8') as outfile:
        for category in sorted_categories:
            outfile.write('\n')
            units = categories[category]
            outfile.write(category.title() + '\n\n')
            for unit in units:
                outfile.write('\t' + unit.name + '\n')

    new_checksum = file_checksum(filename)
    if old_checksum != new_checksum:
        print(f'Saved {len(all_units)} units to {DEST_FILE}')
    else:
        print(f'{filename.name} is already up to date.')


if __name__ == '__main__':
    create_supported_units(DEST_FILE)
