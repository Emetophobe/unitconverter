# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The poise (P) is the unit of dynamic viscosity (absolute viscosity)
# in the centimetre–gram–second system of units (CGS).
poise = Unit(
    name='poise',
    symbols='P',
    aliases='poises',
    category='viscosity',
    factor='1')

# 1 pascal second is equal to 10 poise
pascal_second = Unit(
    name='pascal second',
    symbols=['Pa*s', 'Pa⋅s', 'Pa-s'],
    aliases=['pascal seconds', 'pascal-seconds', 'pascal-second'],
    category='viscosity',
    prefix_index=0,
    factor='0.1')
