# Copyright (c) 2022-2023 Mike Cunningham


import json
from typing import Optional

from unitconverter.exceptions import DefinitionError


def load_dimensions():
    """ Load dimension definitions. """

    filename = 'data/dimensions.json'

    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
    except OSError:
        raise DefinitionError(f'Invalid dimension file: {filename}')

    if not data or not isinstance(data, dict):
        raise DefinitionError(f'Invalid dimension file: {filename}')

    dimensions = {}
    for category, dimen in data.items():
        if category == 'dimensionless':
            dimensions[()] = category
            continue

        # Add base dimension, for example ('area', 1)
        base_dim = {category: 1}
        if base_dim not in dimen:
            dimen.insert(0, base_dim)

        # TODO: calculate permutations, i.e (length, time) vs (time, length)

        for dim in dimen:
            dim_key = dimension_key(dim)
            if dim_key in dimensions:
                original = dimensions[dim_key]
                raise DefinitionError(f'Duplicate dimension: {dim_key} ({category})'
                                      f' (original: {original})')

            dimensions[dim_key] = category

    return dimensions


def dimension_key(dimension: dict) -> tuple:
    """ Create a hashable tuple from a dimension dict. """
    return tuple((key, dimension[key]) for key in sorted(dimension.keys()))


def dimension_name(dimension: dict) -> Optional[str]:
    """ Get dimension name from a dimension dict. Returns None if not found. """
    return DIMENSION_MAP.get(dimension_key(dimension), None)


# Global dimension dictionary
DIMENSION_MAP = load_dimensions()


# Fuel categories can be converted using the convert_fuel() function
FUEL_CATEGORY = ('fuel economy', 'fuel consumption')


# for key, value in DIMENSION_MAP.items():
#    print(value, key)
