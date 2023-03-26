# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import (combinations, METRE_NAMES, LITRE_NAMES, PER_METRE,
                                 PER_LITRE, PER_UKGALLON, PER_USGALLON)


# litre per metre is the base unit
litre_per_metre = Unit(
    name='litre per metre',
    factor='1',
    symbols=['L/m', 'l/m'],
    aliases=combinations(LITRE_NAMES, PER_METRE),
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/litre is equivalent to 1 litre/metre
metre_per_litre = Unit(
    name='metre per litre',
    factor='1',
    symbols=['m/L', 'm/l'],
    aliases=combinations(METRE_NAMES, PER_LITRE),
    prefix_scaling='si',
    prefix_index=0)

# 1 litre/100km = 0.001 litre/metre
litre_per_100km = Unit(
    name='litre per 100km',
    factor='0.00001',
    symbols=['L/100km', 'l/100km'],
    aliases=combinations(LITRE_NAMES, [' per 100km', '/100km']),
    prefix_scaling='si',
    prefix_index=0)


# UK gallons


# 1 foot per uk gallon is roughly 0.067046626881562 litres/metre
foot_per_ukgallon = Unit(
    name='foot per gallon',
    factor='0.067046626881562',
    symbols=['ft/gal', 'ft/ukgal'],
    aliases=combinations(['foot', 'feet'], PER_UKGALLON))

# 1 metre per uk gallon is roughly 0.2199687986 litre/metre
metre_per_ukgallon = Unit(
    name='metre per gallon',
    factor='0.2199687986',
    symbols=['m/gal', 'm/ukgal'],
    aliases=combinations(METRE_NAMES, PER_UKGALLON),
    prefix_scaling='si',
    prefix_index=0)

# 1 mile per uk gallon is roughly 0.0028248108789117 litre/metre
mile_per_ukgallon = Unit(
    name='mile per gallon',
    factor='0.0028248108789117',
    symbols=['mpg', 'ukmpg', 'mi/gal'],
    aliases=combinations(['mile', 'miles'], PER_UKGALLON))


# US gallons


# 1 foot per us gallon is roughly 0.080519999871169 litres/metre
foot_per_usgallon = Unit(
    name='foot per usgallon',
    factor='0.080519999871169',
    symbols='ft/usgal',
    aliases=combinations(['foot', 'feet'], PER_USGALLON))

# 1 metre per us gallon is roughly 0.2641720524 litre/metre
metre_per_usgallon = Unit(
    name='metre per usgallon',
    factor='0.2641720524',
    symbols='m/usgal',
    aliases=combinations(METRE_NAMES, PER_USGALLON),
    prefix_scaling='si',
    prefix_index=0)

# 1 mile per usgallon is roughly 0.0023521442146661 metres/liter
mile_per_usgallon = Unit(
    name='mile per usgallon',
    factor='0.0023521442146661',
    symbols=['usmpg', 'mi/usgal'],
    aliases=combinations(['mile', 'miles'], PER_USGALLON))
