# Copyright (c) 2022-2023 Mike Cunningham


# work in progress
DIMENSION_MAP = {
    'amount of substance/time': 'catalytic activity',
    'electric current/length': 'magnetic field strength',
    'length/time': 'speed',
    'length/time2': 'acceleration',
    'length2': 'area',
    'length3': 'volume',
    'length/volume': 'fuel economy',
    'volume/length': 'fuel consumption',
    'volume/time': 'volumetric flow rate',
}


def get_category(category: str):
    return DIMENSION_MAP.get(category, category)
