# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The pascal second (Pa s) is the SI unit of dynamic or absolute viscosity
pascal_second = Unit(
    name='pascal second',
    factor='1',
    symbols=['Pa*s', 'Pa⋅s', 'Pa-s'],
    aliases=['pascal seconds', 'pascal-seconds', 'pascal-second'],
    category='viscosity',
    prefix_scaling='si',
    prefix_index=0)


# The poise (P) is the unit of dynamic viscosity or absolute viscosity in the
# centimetre–gram–second system of units (CGS).
# 1 poise is equal to 1 pascal second
poise = Unit(
    name='poise',
    factor='0.1',
    symbols='P',
    aliases='poises',
    category='viscosity',
    prefix_scaling='si')
