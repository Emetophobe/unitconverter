# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# litre per metre is the base unit
litre_per_metre = Unit(
    name='litre per metre',
    factor='1',
    symbols=['L/m', 'l/m'],
    aliases=['litres per metre', 'liter per minute', 'litres per minute',
             'litre/metre', 'litres/metre', 'liter/meter', 'liters/meter'],
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/litre is equivalent to 1 litre/metre
metre_per_litre = Unit(
    name='metre per litre',
    factor='1',
    symbols=['m/L', 'm/l'],
    aliases=['metres per litre', 'meters per liter', 'meter per liter', 'metre/litre',
             'metres/litre', 'meter/liter', 'meters/liter'],
    prefix_scaling='si',
    prefix_index=0)

# 1 litre/100km = 0.001 litre/metre
litre_per_100km = Unit(
    name='litre per 100km',
    factor='0.00001',
    symbols=['L/100km', 'l/100km'],
    aliases=['litres per 100km', 'liters per 100km', 'liter per 100km',
             'litre/100km', 'litres/100km', 'liter/100km', 'liters/100km'],
    prefix_scaling='si',
    prefix_index=0)


# UK gallons

# 1 foot per ukgallon is roughly 0.067046626881562 litres/metre
foot_per_ukgallon = Unit(
    name='foot per gallon',
    factor='0.067046626881562',
    symbols=['ft/gal', 'ft/ukgal'],
    aliases=['feet per gallon', 'foot/gallon', 'feet/gallon', 'foot/gal', 'feet/gal'])

# 1 metre per ukgallon is roughly 0.2199687986 litre/metre
metre_per_ukgallon = Unit(
    name='metre per gallon',
    factor='0.2199687986',
    symbols=['m/gal', 'm/ukgal'],
    aliases=['metres per gallon', 'meter per gallon', 'meters per gallon',
             'metre/gallon', 'metres/gallon', 'meter/gallon', 'meters/gallon',
             'metre/gal', 'metres/gal', 'meter/gal', 'meters/gal'],
    prefix_scaling='si',
    prefix_index=0)

# 1 mile per ukgallon is roughly 0.0028248108789117 litre/metre
mile_per_ukgallon = Unit(
    name='mile per gallon',
    factor='0.0028248108789117',
    symbols=['mpg', 'ukmpg', 'mi/gal'],
    aliases=['miles per gallon', 'mile/gallon', 'miles/gallon',
             'miles/gal', 'mile/gal'])


# US gallons


# 1 foot per usgallon is roughly 0.080519999871169 litres/metre
foot_per_usgallon = Unit(
    name='foot per usgallon',
    factor='0.080519999871169',
    symbols='ft/usgal',
    aliases=['feet per usgallon', 'foot/usgallon', 'feet/usgallon',
             'foot/usgal', 'feet/usgal'])

# 1 metre per usgallon is roughly 0.2641720524 litre/metre
metre_per_usgallon = Unit(
    name='metre per usgallon',
    factor='0.2641720524',
    symbols='m/usgal',
    aliases=['metres per usgallon', 'metre/usgallon', 'metres/usgallon',
             'meters/usgallon', 'meter/usgallon', 'metre/usgal',
             'metres/usgal', 'meter/usgal', 'meters/usgal'],
    prefix_scaling='si',
    prefix_index=0)

# 1 mile per usgallon is roughly 0.0023521442146661 metres/liter
mile_per_usgallon = Unit(
    name='mile per usgallon',
    factor='0.0023521442146661',
    symbols=['usmpg', 'mi/usgal'],
    aliases=['miles per usgallon', 'mile/usgallon', 'miles/usgallon',
             'miles/usgal', 'mile/usgal'])
