# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations


# The pascal second (Pa s) is the SI unit of dynamic or absolute viscosity
pascal_second = Unit(
    name='pascal second',
    factor='1',
    symbols=['Pa*s', 'Pa⋅s', 'Pa-s'],
    aliases=['pascal seconds', 'pascal-seconds', 'pascal-second'],
    category='viscosity',
    prefix_scaling='si',
    prefix_index=0)

# The poise (P) is the unit of dynamic viscosity or absolute viscosity
# in the centimetre–gram–second system of units (CGS).
# 1 poise = 0.1 pascal-seconds
poise = Unit(
    name='poise',
    factor='0.1',
    symbols='P',
    aliases='poises',
    category='viscosity',
    prefix_scaling='si')

# 1 gram/foot-second = 0.00328083989501312 pascal-seconds
per_foot_second = combinations([' per ', '/'], ['foot second', 'feet second'])
gram_per_footsecond = Unit(
    name='gram per foot second',
    factor='0.00328083989501312',
    symbols=['g/[ft s]', 'g/ft s', 'g/ft-s'],
    aliases=combinations(['gram', 'grams'], per_foot_second),
    prefix_scaling='si',
    prefix_index=0)

# 1 gram/metre-second = 0.001 pascal-seconds
per_metre_second = combinations([' per ', '/'], ['metre second', 'meter second'])
gram_per_metersecond = Unit(
    name='gram per metre second',
    factor='0.001',
    symbols=['g/[m s]', 'g/m s', 'g/m-s'],
    aliases=combinations(['gram', 'grams'], per_metre_second),
    prefix_scaling='si',
    prefix_index=0)

# 1 slug/foot-second = 47.88025898 pascal-seconds
slug_per_footsecond = Unit(
    name='slug per foot second',
    factor='47.88025898',
    symbols=['slug/[ft s]', 'slug/ft s', 'slug/ft-s'],
    aliases=combinations(['slug', 'slugs'], per_foot_second))


# Cleanup
del per_foot_second
del per_metre_second
