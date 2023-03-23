# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of magnetic flux density
tesla = Unit(
    name='tesla',
    symbols='T',
    aliases='teslas',
    factor='1')

gamma = Unit(
	name='gamma',
	symbols='y',
	aliases='gammas',
	factor='1E-9')

guass = Unit(
	name='guass',
	symbols='G',
	aliases='gausses',
	factor='1E-4')
