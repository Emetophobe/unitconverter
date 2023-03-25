# Copyright (c) 2022-2023 Mike Cunningham


from unitconverter.unit import Unit


# Solid angle

# SI unit
# 1 steradian =  (180/pi)^2 or roughly 3282.8 square degrees
steradian = Unit(
    name='steradian',
    factor='1',
    symbols='sr',
    aliases='steradians',
    category='solid angle')

# 1 square degree = (pi*180)^2 or roughly 0.000304617419786 steradians
square_degree = Unit(
    name='square degree',
    factor='3.04617E-4',
    symbols=['deg^2', 'deg2'],
    aliases='square degrees',
    category='solid angle')

spat = Unit(
    name='spat',
    factor='12.5663706144',
    symbols='sp',
    aliases='spats',
    category='solid angle')

# Plane angle

# SI unit
# 1 radian = 180/pi degrees or roughly 57.295779513 degrees
radian = Unit(
    name='radian',
    factor='1',
    symbols='rad',
    aliases='radians',
    category='plane angle')

# 1 degree = pi/180 radians or roughly 0.0174532925 radians
degree = Unit(
    name='degree',
    factor='0.0174532925',
    symbols=['°', 'deg'],
    aliases='degrees',
    category='plane angle')

# 1 gradian = pi/200 radians or roughly 0.015708 radians
gradian = Unit(
    name='gradian',
    factor='0.015708',
    symbols='gon',
    aliases=['gradians', 'grade', 'grad'],
    category='plane angle')
