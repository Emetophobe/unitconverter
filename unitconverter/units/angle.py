# Copyright (c) 2022-2023 Mike Cunningham


from unitconverter.unit import Unit


# Solid angle

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


# Plane angle

class PlaneAngle(Unit):
    category = 'plane angle'


# The radian is the SI unit of plane angle
# 1 radian = 180/pi degrees or roughly 57.295779513 degrees
radian = PlaneAngle(
    name='radian',
    factor='1',
    symbols='rad',
    aliases='radians',
    prefix_scaling='si')

# 1 degree = pi/180 radians or roughly 0.0174532925 radians
degree = PlaneAngle(
    name='degree',
    factor='0.0174532925',
    symbols=['°', 'deg'],
    aliases='degrees')

# 1 gradian = pi/200 radians or roughly 0.015708 radians
gradian = PlaneAngle(
    name='gradian',
    factor='0.015708',
    symbols='gon',
    aliases=['gradians', 'grade', 'grad'])

# 1 arcsecond = pi / (180 × 3600) = roughly 4.848136957929807e-06 radians
arcsecond = PlaneAngle(
    name='arcsecond',
    factor='4.848136957929807e-06',
    symbols='arcsec',
    aliases='arc second',
    prefix_scaling='si')

# 1 arcminute = pi / (60 x 180) = roughly 0.000290888 radians
arcminute = PlaneAngle(
    name='arcminute',
    factor='0.000290888',
    symbols='arcmin',
    aliases='arc minute')

# 1 turn = 360 degrees = 400 gradians = 2π radians = roughly 6.283185307179586 radians
turn = PlaneAngle(
    name='turn',
    factor='6.283185307179586',
    symbols=['tr', 'pl'])
