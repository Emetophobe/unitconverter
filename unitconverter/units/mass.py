# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit

# SI unit for mass is kilograms (kg) but I use gram (g) for simplicity.
gram = Unit(
    name='gram',
    factor='1',
    symbols='g',
    aliases='grams',
    prefix_scaling='si')

# Metric ton is 1E+6 grams (1,000,000 g)
tonne = Unit(
    name='tonne',
    factor='1E+6',
    symbols='t',
    aliases=['tonnes', 'metric tons', 'metric ton', 'tons', 'ton'],
    prefix_scaling='si')

# 1 ounce is 28.34952 grams
ounce = Unit(
    name='ounce',
    factor='28.34952',
    symbols='oz',
    aliases=['ounces', 'imperial ounces', 'imperial ounce'])

# 1 pound is 453.59237 grams
pound = Unit(
    name='pound',
    factor='453.59237',
    symbols='lbs',
    aliases=['pounds', 'imperial pounds', 'imperial pound'])

# 1 kilopound (kip) = 1000 lbs or 453592.37 grams
kilopound = Unit(
    name='kilopound',
    factor='453592.37',
    symbols=['kip', 'klbs'],
    aliases=['kilopounds', 'imperial kilopounds', 'imperial kilopound'])

# 1 stone = 14 lbs or 6350.29 grams
stone = Unit(
    name='stone',
    factor='6350.29',
    symbols='st',
    aliases=['stones', 'imperial stone'])

# 1 imperial ton = 1016046.91 grams
imperial_ton = Unit(
    name='imperial ton',
    factor='1016046.91',
    symbols='LT',
    aliases=['imperial tons', 'long tons', 'long ton'])

# 1 US ton = 907184.74 grams
us_ton = Unit(
    name='US ton',
    factor='907184.74',
    symbols='ST',
    aliases=['US tons', 'short tons', 'short ton'])

# 1 carat = 0.2 grams
carat = Unit(
    name='carat',
    factor='0.2',
    symbols=['car', 'ct'],
    aliases='carats')

# 1 grain = roughly 0.0647989 grams
grain = Unit(
    name='grain',
    factor='0.0647989',
    symbols='gr',
    aliases='grains')

# 1 drachm = roughly 1.77185 grams
drachm = Unit(
    name='drachm',
    factor='1.77185',
    symbols='dr',
    aliases=['drachms', 'drams', 'dram'])

# 1 pennyweight = roughly 1.55517384 grams
pennyweight = Unit(
    name='pennyweight',
    factor='1.55517384',
    symbols='dwt',
    aliases='pennyweights')

# 1 troy ounce = roughly 31.1035 grams
troy_ounce = Unit(
    name='troy ounce',
    factor='31.1035',
    symbols='ozt',
    aliases='troy ounces')

# 1 troy pound = roughly 373.242 grams
troy_pound = Unit(
    name='troy pound',
    factor='373.242',
    symbols='lbt',
    aliases='troy pounds')
