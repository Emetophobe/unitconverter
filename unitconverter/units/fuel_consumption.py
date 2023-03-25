# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# litre per metre is the base unit
litre_per_metre = Unit(
    name='litre/metre',
    factor='1',
    symbols=['L/m', 'l/m'],
    aliases=['litres/metre', 'liters/meter', 'liter/meter'],
    prefix_scaling='si')

# 1 metre/litre is equivalent to 1 litre/metre
metre_per_litre = Unit(
    name='metre/litre',
    factor='1',
    symbols=['m/L', 'm/l'],
    aliases=['metres/litre', 'meters/liter', 'meter/liter'],
    prefix_scaling='si')

# 1 litre/100km = 0.001 litre/metre
litre_per_100km = Unit(
    name='litre/100km',
    factor='0.00001',
    symbols=['L/100km', 'l/100km'],
    aliases=['litres/100km', 'liters/100km', 'liter/100km'],
    prefix_scaling='si')


# UK gallons

# 1 foot/ukgallon is roughly 0.067046626881562 litres/metre
foot_per_ukgallon = Unit(
    name='foot/gallon',
    factor='0.067046626881562',
    symbols=['ft/gal', 'ft/ukgal'],
    aliases=['feet/gallon', 'foot/gal', 'feet/gal'])

# 1 metre/ukgallon is roughly 0.2199687986 litre/metre
metre_per_ukgallon = Unit(
    name='metre/gallon',
    factor='0.2199687986',
    symbols=['m/gal', 'm/ukgal'],
    aliases=['metres/gallon', 'meter/gallon', 'meters/gallon', 'metres/gal',
             'metre/gal', 'meters/gal', 'meter/gal'],
    prefix_scaling='si')

# 1 mile/ukgallon is roughly 0.0028248108789117 litre/metre
mile_per_ukgallon = Unit(
    name='mile/gallon',
    factor='0.0028248108789117',
    symbols=['mpg', 'ukmpg', 'mi/gal'],
    aliases=['miles/gallon', 'miles/gal', 'mile/gal'])


# US gallons


# 1 foot/usgallon is roughly 0.080519999871169 litres/metre
foot_per_usgallon = Unit(
    name='foot/usgallon',
    factor='0.080519999871169',
    symbols='ft/usgal',
    aliases=['feet/usgallon', 'foot/usgal', 'feet/usgal'])

# 1 metre/usgallon is roughly 0.2641720524 litre/metre
metre_per_usgallon = Unit(
    name='metre/usgallon',
    factor='0.2641720524',
    symbols='m/usgal',
    aliases=['metres/usgallon', 'meters/usgallon', 'meter/usgallon',
             'metre/usgal', 'meter/usgal'],
    prefix_scaling='si')

# 1 mile/usgallon is roughly 0.0023521442146661 metres/liter
mile_per_usgallon = Unit(
    name='mile/usgallon',
    factor='0.0023521442146661',
    symbols=['usmpg', 'mi/usgal'],
    aliases=['miles/usgallon', 'miles/usgal', 'mile/usgal'])
