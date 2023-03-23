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

pascal_second = Unit(
	name='pascal second',
	symbols='Pa*s',
	aliases=['pascal seconds', 'pascal-seconds', 'pascal-second'],
	category='viscosity',
	factor='0.1')
