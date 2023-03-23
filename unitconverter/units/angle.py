# Copyright (c) 2022-2023 Mike Cunningham


from unitconverter.unit import Unit


# Solid angle

# SI unit
# 1 steradian is (180/pi)^2 square degrees or about 3282.8 square degrees
steradian = Unit(
	name='steradian',
	symbols='sr',
	aliases='steradians',
	category='solid angle',
	factor='1')

# 1 square degree is (pi*180)^2 or 0.000304617419786 steradians
square_degree = Unit(
	name='square degree',
	symbols=['deg^2', 'deg2'],
	aliases='square degrees',
	category='solid angle',
	factor='3.04617E-4',
	prefix_scaling='none')

spat = Unit(
	name='spat',
	symbols='sp',
	aliases='spats',
	category='solid angle',
	factor='12.5663706144')

# Plane angle

# SI unit
# 1 radian is 57.295779513 degrees (180/pi)
radian = Unit(
	name='radian',
	symbols='rad',
	aliases='radians',
	category='plane angle',
	factor='1')

# 1 degree is 0.0174532925 radians (pi/180)
degree = Unit(
	name='degree',
	symbols='°',
	aliases='degrees',
	factor='0.0174532925',
	category='plane angle',
	prefix_scaling='none',
)
