# Copyright (c) 2022-2023 Mike Cunningham


# work in progress
DIMENSION_MAP = {
    'length/time2': 'acceleration',
    'length2': 'area',
    'volume/length': 'fuel consumption',
    'length/volume': 'fuel economy',
    'length/time': 'speed',
    'length3': 'volume',
}


def get_category(category: str):
    return DIMENSION_MAP.get(category, category)
