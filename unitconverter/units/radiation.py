# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


### Radioactivity units (becquerel, curie, rutherford)


# SI unit
becquerel = Unit(
    name='becquerel',
    symbols='Bq',
    aliases='becquerels',
    category='radioactivity',
    factor='1')

curie = Unit(
	name='curie',
	symbols='Ci',
	aliases='curies',
    category='radioactivity',
	factor='3.7E+10')

rutherford = Unit(
	name='rutherford',
	symbols='Rd',
	aliases='rutherfords',
    category='radioactivity',
	factor='1E+6',)


### Absorbed dose units (gray, rad)

# SI unit
gray = Unit(
    name='gray',
    symbols='Gy',
    aliases='grays',
    category='absorbed dose',
    factor='1')

us_rad = Unit(
    name='US rad',
    symbols='usrad',  # rad is used by radian
    aliases='US rads',
    category='absorbed dose',
    factor='0.01')


### Effective dose units (sievert, roentgen)

# SI unit
sievert = Unit(
    name='sievert',
    symbols='Sv',
    aliases='sieverts',
    category='effective dose',
    factor='1')

roentgen = Unit(
	name='roentgen',
	symbols='rem',
	aliases=['roentgens', 'roentgen equivalent man'],
    category='effective dose',
    factor='0.01')
