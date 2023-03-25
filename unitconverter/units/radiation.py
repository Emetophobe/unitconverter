# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


### Radioactivity (becquerel, curie, rutherford)


# The becquerel is the SI unit of radioactivity
becquerel = Unit(
    name='becquerel',
    factor='1',
    symbols='Bq',
    aliases='becquerels',
    category='radioactivity',
    prefix_scaling='si')

# 1 curie = 3.7E+10 becquerel
curie = Unit(
    name='curie',
    factor='3.7E+10',
    symbols='Ci',
    aliases='curies',
    category='radioactivity',
    prefix_scaling='si')

# 1 rutherford = 1 MBq or 1E+6 becquerel
rutherford = Unit(
    name='rutherford',
    factor='1E+6',
    symbols='Rd',
    aliases='rutherfords',
    category='radioactivity')


### Absorbed dose (gray, rad)


# The gray is the SI unit of absorbed dose
gray = Unit(
    name='gray',
    factor='1',
    symbols='Gy',
    aliases='grays',
    category='absorbed dose',
    prefix_scaling='si')

# 1 rad = 0.01 gray
us_rad = Unit(
    name='US rad',
    factor='0.01',
    symbols='usrad',  # rad is used by radian
    aliases='US rads',
    category='absorbed dose')


### Effective dose (sievert, roentgen)


# The sivert is the SI unit of effective dose
sievert = Unit(
    name='sievert',
    factor='1',
    symbols='Sv',
    aliases='sieverts',
    category='effective dose',
    prefix_scaling='si')

# 1 roentgen = 0.01 sievert
roentgen = Unit(
    name='roentgen',
    factor='0.01',
    symbols='rem',
    aliases=['roentgens', 'roentgen equivalent man'],
    category='effective dose',
    prefix_index=0)
