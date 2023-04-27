# Copyright (c) 2022-2023 Mike Cunningham


# work in progress
DIMENSION_MAP = {
    'amount of substance/time': 'catalytic activity',
    'length/time': 'speed',
    'length/time2': 'acceleration',
    'length2': 'area',
    'length3': 'volume',
    'length/volume': 'fuel economy',
    'volume/length': 'fuel consumption',
}


def get_category(category: str):
    return DIMENSION_MAP.get(category, category)
