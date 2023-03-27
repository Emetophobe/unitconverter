# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, METRE_NAMES, LITRE_NAMES, PER_METRE


class FuelConsumption(Unit):
    category = 'fuel consumption'


# litre per metre is the base unit
litre_per_metre = FuelConsumption(
    name='litre per metre',
    factor='1',
    symbols=['L/m', 'l/m'],
    aliases=combinations(LITRE_NAMES, PER_METRE),
    prefix_scaling='si',
    prefix_index=0)

# 1 litre/100km = 0.001 litre/metre
litre_per_100km = FuelConsumption(
    name='litre per 100km',
    factor='0.00001',
    symbols=['L/100km', 'l/100km'],
    aliases=combinations(LITRE_NAMES, [' per 100km', '/100km']),
    prefix_scaling='si',
    prefix_index=0)


# imperial gallons
per_gallon = combinations([' per ', '/'], ['imperial gallon', 'gallon', 'gal'])


# 1 foot per gallon = roughly 14.915 litres/metre
foot_per_gallon = FuelConsumption(
    name='foot per gallon',
    factor='14.915',
    symbols='ft/gal',
    aliases=combinations(['foot', 'feet'], per_gallon))

# 1 metre per gallon = roughly 4.5460992939 litre/metre
metre_per_gallon = FuelConsumption(
    name='metre per gallon',
    factor='4.5460992939',
    symbols='m/gal',
    aliases=combinations(METRE_NAMES, per_gallon),
    prefix_scaling='si',
    prefix_index=0)

# 1 mile per gallon = roughly 0.0028248094 litre/metre
mile_per_gallon = FuelConsumption(
    name='mile per gallon',
    factor='0.0028248094',
    symbols=['mpg', 'mi/gal'],
    aliases=combinations(['mile', 'miles'], per_gallon))


# US liquid gallons
per_gallon = combinations([' per ', '/'], ['usgallon', 'usgal'])


# 1 foot/usgallon = roughly 12.4193301 litres/metre
foot_per_usgallon = FuelConsumption(
    name='foot per usgallon',
    factor='12.4193',
    symbols='ft/usgal',
    aliases=combinations(['foot', 'feet'], per_gallon))

# 1 metre/usgallon = roughly 3.7854117834 litre/metre
metre_per_usgallon = FuelConsumption(
    name='metre per usgallon',
    factor='3.7854117834',
    symbols='m/usgal',
    aliases=combinations(METRE_NAMES, per_gallon),
    prefix_scaling='si',
    prefix_index=0)

# 1 mile/usgallon = roughly 0.0023521458 metres/liter
mile_per_usgallon = FuelConsumption(
    name='mile per usgallon',
    factor='0.0023521458',
    symbols=['usmpg', 'mi/usgal'],
    aliases=combinations(['mile', 'miles'], per_gallon))


# Cleanup
del per_gallon
