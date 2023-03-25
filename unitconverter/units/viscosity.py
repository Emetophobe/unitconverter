# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The poise (P) is the unit of dynamic viscosity (absolute viscosity)
# in the centimetre–gram–second system of units (CGS).
poise = Unit(
    name='poise',
    factor='1',
    symbols='P',
    aliases='poises',
    category='viscosity',
    prefix_scaling='si')

# 1 pascal second is equal to 10 poise
pascal_second = Unit(
    name='pascal second',
    factor='0.1',
    symbols=['Pa*s', 'Pa⋅s', 'Pa-s'],
    aliases=['pascal seconds', 'pascal-seconds', 'pascal-second'],
    category='viscosity',
    prefix_scaling='si',
    prefix_index=0)
