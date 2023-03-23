# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit for mass is the kilogram
# I use gram for convenience
gram = Unit(
	name='gram',
	symbols='g',
	aliases='grams',
	factor='1')

ounce = Unit(
	name='ounce',
	symbols='oz',
	aliases='ounces',
	factor='28.34952')

pound = Unit(
	name='pound',
	symbols='lbs',
	aliases='pounds',
	factor='453.592')

stone = Unit(
	name='stone',
	symbols='st',
	aliases='stones',
	factor='6350.29')

imperial_ton = Unit(
	name='imperial ton',
	symbols='LT',
	aliases=['imperial tons', 'long tons', 'long ton'],
	factor='1016046.9')

us_ton = Unit(
	name='US ton',
	symbols='ST',
	aliases=['US tons', 'short tons', 'short ton'],
	factor='907184.74')

tonne = Unit(
	name='tonne',
	symbols='t',
	aliases=['tonnes', 'metric tons', 'metric ton'],
	factor='1E+6')

carat = Unit(
	name='carat',
	symbols=['car', 'ct'],
	aliases='carats',
	factor='0.2')

grain = Unit(
	name='grain',
	symbols='gr',
	aliases='grains',
	factor='0.0647989')

drachm = Unit(
	name='drachm',
	symbols='dr',
	aliases=['drachms', 'drams', 'dram'],
	factor='1.77185')

pennyweight = Unit(
	name='pennyweight',
	symbols='dwt',
	aliases='pennyweights',
	factor='1.55517384')

troy_ounce = Unit(
	name='troy ounce',
	symbols='ozt',
	aliases='troy ounces',
	factor='31.1035')

troy_pound = Unit(
	name='troy pound',
	symbols='lbt',
	aliases='troy pounds',
	factor='373.242')
