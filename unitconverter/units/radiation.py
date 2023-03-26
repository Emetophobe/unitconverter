# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# Radioactivity (becquerel, curie, rutherford)
class Radioactivity(Unit):
    category = 'radioactivity'


# The becquerel is the SI unit of radioactivity
becquerel = Radioactivity(
    name='becquerel',
    factor='1',
    symbols='Bq',
    aliases='becquerels',
    prefix_scaling='si')

# 1 curie = 3.7E+10 becquerel
curie = Radioactivity(
    name='curie',
    factor='3.7E+10',
    symbols='Ci',
    aliases='curies',
    prefix_scaling='si')

# 1 rutherford = 1 MBq or 1E+6 becquerel
rutherford = Radioactivity(
    name='rutherford',
    factor='1E+6',
    symbols='Rd',
    aliases='rutherfords')


# Absorbed dose (gray, rad)
class AbsorbedDose(Unit):
    category = 'absorbed dose'


# The gray is the SI unit of absorbed dose
gray = AbsorbedDose(
    name='gray',
    factor='1',
    symbols='Gy',
    aliases='grays',
    prefix_scaling='si')

# 1 rad = 0.01 gray
us_rad = AbsorbedDose(
    name='US rad',
    factor='0.01',
    symbols='usrad',  # rad is used by radian
    aliases='US rads')


# Effective dose (sievert, roentgen)
class EffectiveDose(Unit):
    category = 'effective dose'


# The sivert is the SI unit of effective dose
sievert = EffectiveDose(
    name='sievert',
    factor='1',
    symbols='Sv',
    aliases='sieverts',
    prefix_scaling='si')

# 1 roentgen = 0.01 sievert
roentgen = EffectiveDose(
    name='roentgen',
    factor='0.01',
    symbols='rem',
    aliases=['roentgens', 'roentgen equivalent man'],
    prefix_index=0)
