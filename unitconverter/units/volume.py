# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.units import length, area


# The cubic metre (m^3) is the SI unit of volume
cubic_metre = Unit(
    name='cubic metre',
    factor='1',
    symbols=['m^3', 'm3'],
    aliases=['cubic metres', 'cubic meters', 'cubic meter', 'metre^3', 'metre3'],
    power=3,
    prefix_scaling='si')

# 1 litre = 0.001 m^3 (1000 litres = 1 m^3)
litre = Unit(
    name='litre',
    factor='1E-3',
    symbols=['L', 'l'],
    aliases=['litres', 'liters', 'liter'],
    prefix_scaling='si')

# 1 metric cup = 0.00025 m^3
cup = Unit(
    name='cup',
    factor='0.00025',
    aliases=['cups', 'metric cups', 'metric cup'])

# 1 metric tbps = 1.5E-5 m^3
tablespoon = Unit(
    name='tablespoon',
    factor='1.5E-5',
    symbols='tbsp',
    aliases=['tablespoons', 'metric tablespoons', 'metric tablespoon'])

# 1 metric teaspoon = 5E-6 m^3
teaspoon = Unit(
    name='teaspoon',
    factor='5E-6',
    symbols='tsp',
    aliases=['teaspoons', 'metric teaspoons', 'metric teaspoon'])

# 1 stere = 1 m^3
stere = Unit(
    name='stere',
    factor='1',
    aliases=['steres', 'stères', 'stère'])

# 1 drop = 5E-8 m^3
drop = Unit(
    name='drop',
    factor='5E-8',
    symbols='gt',
    aliases='drops')


# Imperial units


# 1 cubic inch is roughly 0.000016387064 m^3
cubic_inch = Unit(
    name='cubic inch',
    factor=length.inch.factor ** 3,
    symbols=['cu in', 'in^3', 'in3'],
    aliases='cubic inches')

# 1 cubic foot is roughly 0.028316846592 m^3
cubic_foot = Unit(
    name='cubic foot',
    factor=length.foot.factor ** 3,
    symbols=['cu ft', 'ft^3', 'ft3'],
    aliases='cubic feet')

# 1 cubic yard is roughly 0.764554857984 m^3
cubic_yard = Unit(
    name='cubic yard',
    factor=length.yard.factor ** 3,
    symbols=['cu yd', 'yd^3', 'yd3'],
    aliases='cubic yards')

# 1 cubic mile is roughly 4,168,181,825.440579584 m^3
cubic_mile = Unit(
    name='cubic mile',
    factor=length.mile.factor ** 3,
    symbols=['cu mi', 'mi^3', 'mi3'],
    aliases='cubic miles')

# 1 acre inch = 1 acre × 1 inch or 102.79015312896 m^3
acre_inch = Unit(
    name='acre-inch',
    factor=area.acre.factor * length.inch.factor,
    symbols=['ac*in', 'ac-in', 'ac⋅in'],
    aliases=['acre-inches', 'acre-in'])

# 1 acre foot = 1 acre × 1 foot or 1233.48183754752 m^3
acre_foot = Unit(
    name='acre-foot',
    factor=area.acre.factor * length.foot.factor,
    symbols=['ac*ft', 'ac-ft' 'ac⋅ft'],
    aliases='acre-feet')

# 1 imperial gill = roughly 0.0001420653 m^3
imperial_gill = Unit(
    name='imperial gill',
    factor='0.0001420653',
    symbols='gi',
    aliases=['gills', 'gill', 'imperial gills'])

# 1 imperial cup = roughly 0.0002841306 m^3
imperial_cup = Unit(
    name='imperial cup',
    factor='0.0002841306',
    aliases=['imperial cups', 'impcups', 'impcup'])

# 1 imperial bushel = roughly 0.03636872 m^3
imperial_bushel = Unit(
    name='imperial bushel',
    factor='0.03636872',
    symbols=['bsh', 'bu'],
    aliases=['bushels', 'bushel', 'imperial bushels'])

# 1 imperial fluid ounce = roughly 2.84130625E-5 m^3
imperial_fluid_ounce = Unit(
    name='imperial fluid ounce',
    factor='2.84130625E-5',
    symbols=['fl oz', 'imp fl oz', 'impfloz'],
    aliases=['fluid ounces', 'fluid ounce', 'imperial fluid ounces'])

# 1 imperial gallon = roughly 0.00454609 m^3
imperial_gallon = Unit(
    name='imperial gallon',
    factor='0.00454609',
    symbols='gal',
    aliases=['gallons', 'gallon', 'imperial gallons'])

# 1 imperial pint = roughly 0.0005682615 m^3
imperial_pint = Unit(
    name='imperial pint',
    factor='0.0005682615',
    symbols='pt',
    aliases=['pints', 'pint', 'imperial pints'])

# 1 imperial quart = roughly 0.0011365225 m^3
imperial_quart = Unit(
    name='imperial quart',
    factor='0.0011365225',
    symbols='qt',
    aliases=['quarts', 'quart', 'imperial quarts'])

# 1 imperial tablespoon = 1.77582E-5 m^3
imperial_tablespoon = Unit(
    name='imperial tablespoon',
    factor='1.77582E-5',
    symbols=['tbsp-imp', 'tbsp-uk'],
    aliases=['imperial tablespoons', 'imperial tbsp'])

# 1 imperial teaspoon = 5.919388E-6 m^3
imperial_teaspoon = Unit(
    name='imperial teaspoon',
    factor='5.919388E-6',
    symbols=['tsp-imp', 'tsp-uk'],
    aliases=['imperial teaspoons', 'imperial tsp'])


# US customary and survey units


# 1 US gill = roughly 0.0001182941 m^3
us_gill = Unit(
    name='US gill',
    factor='0.0001182941',
    symbols='gi-us',
    aliases=['US gills', 'usgills', 'usgill'])

# 1 US cup = roughly 0.000236588 m^3
us_cup = Unit(
    name='US cup',
    factor='0.000236588',
    aliases=['US cups', 'uscups', 'uscup'])

# 1 US bushel = roughly 0.0352391 m^3
us_bushel = Unit(
    name='US bushel',
    factor='0.0352391',
    symbols=['usbsh', 'usbu'],
    aliases='US bushels')

# 1 US fluid ounce = roughly 2.95735E-5 m^3
us_fluid_ounce = Unit(
    name='US fluid ounce',
    factor='2.95735E-5',
    symbols=['us fl. oz', 'us fl oz', 'usfloz'],
    aliases='US fluid ounces')

# 1 US liquid gallon = roughly 0.003785411784 m^3
us_liquid_gallon = Unit(
    name='US liquid gallon',
    factor='0.003785411784',
    symbols=['usliquidgal', 'liquidgal', 'usgal'],
    aliases=['US liquid gallons', 'US liquid gal', 'US gal'])

# 1 US dry gallon = roughly 0.00440488 m^3
us_dry_gallon = Unit(
    name='US dry gallon',
    factor='0.00440488',
    symbols=['usdrygal', 'drygal'],
    aliases=['US dry gallons', 'US dry gal'])

# 1 US liquid pint = roughly 0.00473176 m^3
us_liquid_pint = Unit(
    name='US liquid pint',
    factor='0.000473176',
    symbols=['usliquidpt', 'liquidpt', 'uspt'],
    aliases=['US liquid pints', 'US pints', 'US pt'])

# 1 US dry pint = roughly 0.000550610475 m^3
us_dry_pint = Unit(
    name='US dry pint',
    factor='0.000550610475',
    symbols=['usdrypt', 'drypt'],
    aliases=['US dry pints', 'US dry pt'])

# 1 US liquid quart = roughly 0.000946353 m^3
us_liquid_quart = Unit(
    name='US liquid quart',
    factor='0.000946353',
    symbols=['usliquidqt', 'liquidqt', 'usqt'],
    aliases=['US liquid quarts', 'US liquid qt', 'US quarts', 'US quart'])

# 1 US dry quart = roughly 0.0011012107 m^3
us_dry_quart = Unit(
    name='US dry quart',
    factor='0.0011012107',
    symbols=['usdryqt', 'dryqt'],
    aliases=['US dry quarts', 'US dry qt'])

# 1 US tablespoon = roughly 1.47868E-5 m^3
us_tablespoon = Unit(
    name='US tablespoon',
    factor='1.47868E-5',
    symbols='ustbsp',
    aliases=['US tablespoons', 'US tbsp'])

# 1 US teaspoon = roughly 4.92892E-6 m^3
us_teaspoon = Unit(
    name='US teaspoon',
    factor='4.92892E-6',
    symbols='ustsp',
    aliases=['US teaspoons', 'US tsp'])

# 1 US survey acre-foot = roughly 1233.489238468149 m^3
us_survey_acre_foot = Unit(
    name='US survey acre-foot',
    factor=area.us_survey_acre.factor * length.us_survey_foot.factor,
    symbols=['us ac*ft', 'usft3', 'usft^3'],
    aliases='US survey acre-feet')
