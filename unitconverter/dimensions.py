# Copyright (c) 2022-2023 Mike Cunningham


import json
from typing import Optional

from unitconverter.exceptions import DefinitionError
from unitconverter.formatting import format_display_name


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

        # Add base dimension, i.e ('area', 1)
        base_dim = {category: 1}
        if base_dim not in dimen:
            dimen.insert(0, base_dim)

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


def dimension_name(dimensions: dict) -> Optional[str]:
    """ Create a dimension name from a dictionary of dimensions. """
    # Search the dimension map for a category name
    category = DIMENSION_MAP.get(dimension_key(dimensions), None)

    # Fallback to creating the category name from the unit dimensions
    if not category:
        category = format_display_name(dimensions)

    if not category:
        return 'dimensionless'

    return category


# Global dimension dictionary
DIMENSION_MAP = load_dimensions()


# Fuel categories can be converted using the convert_fuel() function
FUEL_CATEGORY = ('fuel economy', 'fuel consumption')


# for key, value in DIMENSION_MAP.items():
#     print(value, key)
