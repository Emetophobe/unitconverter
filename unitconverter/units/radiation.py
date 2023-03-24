# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


### Radioactivity (becquerel, curie, rutherford)


# The becquerel is the SI unit of radioactivity
becquerel = Unit(
    name='becquerel',
    symbols='Bq',
    aliases='becquerels',
    category='radioactivity',
    factor='1')

# 1 curie = 3.7E+10 becquerel
curie = Unit(
    name='curie',
    symbols='Ci',
    aliases='curies',
    category='radioactivity',
    factor='3.7E+10')

# 1 rutherford = 1E+6 becquerel
rutherford = Unit(
    name='rutherford',
    symbols='Rd',
    aliases='rutherfords',
    category='radioactivity',
    factor='1E+6')


### Absorbed dose (gray, rad)


# The gray is the SI unit of absorbed dose
gray = Unit(
    name='gray',
    symbols='Gy',
    aliases='grays',
    category='absorbed dose',
    factor='1')

# 1 rad = 0.01 gray
us_rad = Unit(
    name='US rad',
    symbols='usrad',  # rad is used by radian
    aliases='US rads',
    category='absorbed dose',
    factor='0.01')


### Effective dose (sievert, roentgen)


# The sivert is the SI unit of effective dose
sievert = Unit(
    name='sievert',
    symbols='Sv',
    aliases='sieverts',
    category='effective dose',
    factor='1')

# 1 roentgen = 0.01 sievert
roentgen = Unit(
    name='roentgen',
    symbols='rem',
    aliases=['roentgens', 'roentgen equivalent man'],
    category='effective dose',
    factor='0.01')
