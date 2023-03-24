# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# decibel is the base unit
decibel = Unit(
	name='decibel',
	symbols='dB',
	aliases='decibels',
	factor='1')

# 1 bel = 10 decibels
bel = Unit(
	name='bel',
	aliases='bels',
	factor='10')

# 1 neper = 8.686 decibels
neper = Unit(
	name='neper',
	symbols='Np',
	aliases='nepers',
	factor='8.686')
