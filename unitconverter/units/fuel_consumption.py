# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# litre per minute is the base unit
litre_per_metre = Unit(
    name='litre per metre',
    factor='1',
    symbols=['L/m', 'l/m'],
    aliases=['litres per metre', 'liters/metre', 'liter/metre'],
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/litre equals 1 litre/metre
metre_per_litre = Unit(
    name='metre per litre',
    factor='1',
    symbols=['m/L', 'm/l'],
    aliases=['metres per litre', 'metres/liter', 'metre/liter'],
    prefix_scaling='si',
    prefix_index=0)

# 1 litre/100km = 100,000 metres/litre
litre_per_100km = Unit(
    name='litre per 100km',
    factor='100000',
    symbols=['L/100km', 'l/100km'],
    aliases=['litres per 100km', 'liters/100km', 'liter/100km'],
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/UK gallon = 0.2199687986 metres/litre
metre_per_uk_gallon = Unit(
    name='metre per UK gallon',
    factor='0.2199687986',
    symbols='m/ukgal',
    aliases=['metres per UK gallon', 'metre/ukgallon', 'metre/ukgal'],
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/US gallon = 0.2641720524 metres/litre
metre_per_us_gallon = Unit(
    name='metre per US gallon',
    factor='0.2641720524',
    symbols='m/usgal',
    aliases=['metres per US gallon', 'metre/usgallon', 'metre/usgal'],
    prefix_scaling='si',
    prefix_index=0)

# 1 UK gallon/mile = 354.00619 metres/litre
uk_gallon_per_mile = Unit(
    name='UK gallon per mile',
    factor='354.00619',
    symbols=['ukgal/mi', 'gal/mi (UK)'],
    aliases=['UK gallons per mile', 'ukgallon/mile', 'ukgal/mile'])

# 1 UK mile/gallon = 354.00619 metres/litre
uk_mile_per_gallon = Unit(
    name='mile per UK gallon',
    factor='354.00619',
    symbols= ['mpg (UK)', 'mi/gal (UK)'],
    aliases=['miles per UK gallon', 'miles/ukgallon', 'miles/ukgal'])

# 1 US gallon/mile = 425.1437075 metres/litre
us_gallon_per_mile = Unit(
    name='US gallon per mile',
    factor='425.1437075',
    symbols=['usgal/mi', 'gal/mi (US)'],
    aliases=['US gallons per mile', 'usgallon/mile', 'usgal/mile'])

# 1 mile/US gallon = 425.1437075 metres/litre
us_mile_per_gallon = Unit(
    name='mile per US gallon',
    factor='425.1437075',
    symbols = ['mpg (US)', 'mi/gal (US)'],
    aliases=['miles per US gallon', 'miles/usgallon', 'miles/usgal'])
