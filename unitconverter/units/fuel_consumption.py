# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# meter/liter is the base unit
meter_per_liter = Unit(
    name='meter per liter',
    symbols=['m/L', 'm/l'],
    aliases=['meters per liter', 'meters/liter', 'meter/liter'],
    factor='1')

# 1 liter/meter is equal to 1 meter/liter
liter_per_meter = Unit(
    name='liter per meter',
    symbols=['L/m', 'l/m'],
    aliases=['liters per meter', 'liters/meter', 'liter/meter'],
    factor='1')

# 1 liter/100km = 100,000 meters/liter
liter_per_100km = Unit(
    name='liter per 100km',
    symbols=['L/100km', 'l/100km'],
    aliases=['liters per 100km', 'liters/100km', 'liter/100km'],
    factor='100000')

# 1 meter/UK gallon = 0.2199687986 meters/liter
meter_per_uk_gallon = Unit(
    name='meter per UK gallon',
    symbols='m/ukgal',
    aliases=['meters per UK gallon', 'meter/ukgallon', 'meter/ukgal'],
    factor='0.2199687986')

# 1 meter/US gallon = 0.2641720524 meters/liter
meter_per_us_gallon = Unit(
    name='meter per US gallon',
    symbols='m/usgal',
    aliases=['meters per US gallon', 'meter/usgallon', 'meter/usgal'],
    factor='0.2641720524')

# 1 UK gallon/mile = 354.00619 meters/liter
uk_gallon_per_mile = Unit(
    name='UK gallon per mile',
    symbols=['ukgal/mi', 'gal/mi (UK)'],
    aliases=['UK gallons per mile', 'ukgallon/mile', 'ukgal/mile'],
    factor='354.00619')

# 1 UK mile/gallon = 354.00619 meters/liter
uk_mile_per_gallon = Unit(
    name='mile per UK gallon',
    symbols= ['mpg (UK)', 'mi/gal (UK)'],
    aliases=['miles per UK gallon', 'miles/ukgallon', 'miles/ukgal'],
    factor='354.00619')

# 1 US gallon/mile = 425.1437075 meters/liter
us_gallon_per_mile = Unit(
    name='US gallon per mile',
    symbols=['usgal/mi', 'gal/mi (US)'],
    aliases=['US gallons per mile', 'usgallon/mile', 'usgal/mile'],
    factor='425.1437075')

# 1 US mile/gallon = 425.1437075 meters/liter
us_mile_per_gallon = Unit(
    name='mile per US gallon',
    symbols = ['mpg (US)', 'mi/gal (US)'],
    aliases=['miles per US gallon', 'miles/usgallon', 'miles/usgal'],
    factor='425.1437075')
