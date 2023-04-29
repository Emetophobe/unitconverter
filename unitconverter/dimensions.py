# Copyright (c) 2022-2023 Mike Cunningham


# work in progress
DIMENSION_MAP = {
    'amount of substance/time': 'catalytic activity',
    'electric current/length': 'magnetic field strength',
    'length/time': 'speed',
    'length/time^2': 'acceleration',
    'length^2': 'area',
    'length*length': 'area',
    'length^3': 'volume',
    'length*length*length': 'volume',
    'length/volume': 'fuel economy',
    'volume/length': 'fuel consumption',
    'volume/time': 'volumetric flow rate',
}


# Fuel categories can be converted using the convert_fuel() function
fuel_categories = ('fuel economy', 'fuel consumption')


def get_category(category: str):
    return DIMENSION_MAP.get(category, category)
