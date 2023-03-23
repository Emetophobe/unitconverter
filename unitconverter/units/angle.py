# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# Solid angle

# SI unit
steradian = Unit(
	name='steradian',
	symbols='sr',
	aliases='steradians',
	category='solid angle',
	factor='1')

square_degree = Unit(
	name='square degree',
	symbols=['deg^2', 'deg2'],
	aliases='square degrees',
	category='solid angle',
	factor='3.04617E-4')

spat = Unit(
	name='spat',
	symbols='sp',
	aliases='spats',
	category='solid angle',
	factor='12.5663706144')

# Plane angle

# SI unit
radian = Unit(
	name='radian',
	symbols='rad',
	aliases='radians',
	category='plane angle',
	factor='1')
