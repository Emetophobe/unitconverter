# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit

# SI unit for mass is kilograms (kg) but I use gram (g) for simplicity.
gram = Unit(
	name='gram',
	symbols='g',
	aliases='grams',
	factor='1')

# 1 ounce is 28.34952 grams
ounce = Unit(
	name='ounce',
	symbols='oz',
	aliases=['ounces', 'imperial ounces', 'imperial ounce'],
	factor='28.34952')

# 1 pound is 453.59237 grams
pound = Unit(
	name='pound',
	symbols='lbs',
	aliases=['pounds', 'imperial pounds', 'imperial pound'],
	factor='453.59237')

# 1 kilopound (kip) = 1000 lbs or 453592.37 grams
kilopound = Unit(
	name='kilopound',
	symbols='kip',
	aliases='kilopounds',
	factor='453592.37')

# 1 stone = 14 lbs or 6350.29 grams
stone = Unit(
	name='stone',
	symbols='st',
	aliases=['stones', 'imperial stone'],
	factor='6350.29')

# Metric ton is 1E+6 grams (1,000,000 g)
tonne = Unit(
	name='tonne',
	symbols='t',
	aliases=['tonnes', 'metric tons', 'metric ton', 'tons', 'ton'],
	factor='1E+6')

# 1 imperial ton = 1016046.91 grams
imperial_ton = Unit(
	name='imperial ton',
	symbols='LT',
	aliases=['imperial tons', 'long tons', 'long ton'],
	factor='1016046.91')

# 1 US ton = 907184.74 grams
us_ton = Unit(
	name='US ton',
	symbols='ST',
	aliases=['US tons', 'short tons', 'short ton'],
	factor='907184.74')

# 1 carat = 0.2 grams
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
