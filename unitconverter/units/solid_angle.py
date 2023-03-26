# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class SolidAngle(Unit):
    category = 'solid angle'


# The steradian is the SI unit of solid angle
# 1 steradian is (180/pi)^2 square degrees or roughly 3282.8 square degrees
steradian = SolidAngle(
    name='steradian',
    factor='1',
    symbols='sr',
    aliases=['steradians', 'square radian', 'square radians'],
    prefix_scaling='si',
    prefix_index=0)

# 1 square degree is (pi/180)^2 steradian or roughly 3.04617E−4 steradians
square_degree = SolidAngle(
    name='square degree',
    factor='3.04617E-4',
    symbols=['deg^2', 'deg2'],
    aliases='square degrees')

# 1 spat is equal 4π steradians or roughly 12.5663706144 steradian
spat = SolidAngle(
    name='spat',
    factor='12.5663706144',
    symbols='sp',
    aliases='spats')
