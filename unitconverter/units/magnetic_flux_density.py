# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# Tesla is the SI unit of magnetic flux density
tesla = Unit(
	name='tesla',
	symbols='T',
	aliases='teslas',
	factor='1')

# 1 gamma = 1E-9 teslas
gamma = Unit(
	name='gamma',
	symbols='y',
	aliases='gammas',
	factor='1E-9')

# 1 guass = 1E-4 teslas
guass = Unit(
	name='guass',
	symbols='G',
	aliases='gausses',
	factor='1E-4')
