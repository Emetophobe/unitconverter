#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import sys
sys.path.append('.')  # is there a better way?
from unitconverter.units import Units  # noqa

DEST_FILE = 'docs/supported_units.txt'


def create_supported_units(filename):
    """ Generate a text file of all supported units. """
    all_units = Units()
    categories = all_units.get_units()
    sorted_categories = sorted(categories.keys())

    with open(filename, 'w', encoding='utf-8') as outfile:
        for category in sorted_categories:
            outfile.write('\n')
            units = categories[category]
            outfile.write(category.title() + '\n\n')
            for unit in units:
                outfile.write('\t' + unit.name + '\n')

        print(f'Saved {len(all_units)} units to {DEST_FILE}')


if __name__ == '__main__':
    create_supported_units(DEST_FILE)
