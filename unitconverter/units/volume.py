# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.units import length, area


# The cubic meter (m^3) is the SI unit of volume
cubic_meter = Unit(
	name='cubic meter',
	symbols=['m^3', 'm3'],
	aliases=['cubic meters', 'cubic metres', 'cubic metre', 'meter^3', 'meter3'],
	factor='1',
	power=3)

# 1 liter = 0.001 m^3 (1000 liters = 1 m^3)
liter = Unit(
	name='liter',
	symbols=['L', 'l'],
	aliases=['liters', 'litres', 'litre'],
	factor='1E-3')

# 1 cubic inch is roughly 0.000016387064 m^3
cubic_inch = Unit(
	name='cubic inch',
	symbols=['cu in', 'in^3', 'in3'],
	aliases='cubic inches',
	factor=length.inch.factor ** 3)

# 1 cubic foot is roughly 0.028316846592 m^3
cubic_foot = Unit(
	name='cubic foot',
	symbols=['cu ft', 'ft^3', 'ft3'],
	aliases='cubic feet',
	factor=length.foot.factor ** 3)

# 1 cubic yard is roughly 0.764554857984 m^3
cubic_yard = Unit(
	name='cubic yard',
	symbols=['cu yd', 'yd^3', 'yd3'],
	aliases='cubic yards',
	factor=length.yard.factor ** 3)

# 1 cubic mile is roughly 4,168,181,825.440579584 m^3
cubic_mile = Unit(
	name='cubic mile',
	symbols=['cu mi', 'mi^3', 'mi3'],
	aliases='cubic miles',
	factor=length.mile.factor ** 3)

# 1 acre inch = 1 acre × 1 inch or 102.79015312896 m^3
acre_inch = Unit(
	name='acre-inch',
	symbols=['ac*in', 'ac-in', 'acin'],
	aliases=['acre-inches', 'acre-in'],
	factor=area.acre.factor * length.inch.factor)

# 1 acre foot = 1 acre × 1 foot or 1233.48183754752 m^3
acre_foot = Unit(
	name='acre-foot',
	symbols=['ac*ft', 'acft'],
	aliases='acre-feet',
	factor=area.acre.factor * length.foot.factor)

# 1 metric cup = 0.00025 m^3
cup = Unit(
	name='cup',
	aliases=['cups', 'metric cups', 'metric cup'],
	factor='0.00025')

# 1 metric tbps = 1.5E-5 m^3
tablespoon = Unit(
	name='tablespoon',
	symbols='tbsp',
	aliases=['tablespoons', 'metric tablespoons', 'metric tablespoon'],
	factor='1.5E-5')

# 1 metric teaspoon = 5E-6 m^3
teaspoon = Unit(
	name='teaspoon',
	symbols='tsp',
	aliases=['teaspoons', 'metric teaspoons', 'metric teaspoon'],
	factor='5E-6')

# 1 stere = 1 m^3
stere = Unit(
	name='stere',
	aliases=['steres', 'stères', 'stère'],
	factor='1')

# 1 drop = 5E-8 m^3
drop = Unit(
	name='drop',
	symbols='gt',
	aliases='drops',
	factor='5E-8')


# Imperial units


# 1 imperial gill = roughly 0.0001420653 m^3
imperial_gill = Unit(
	name='imperial gill',
	symbols='gi',
	aliases=['gills', 'gill', 'imperial gills'],
	factor='0.0001420653')

# 1 imperial cup = roughly 0.0002841306 m^3
imperial_cup = Unit(
	name='imperial cup',
	aliases=['imperial cups', 'impcups', 'impcup'],
	factor='0.0002841306')

# 1 imperial bushel = roughly 0.03636872 m^3
imperial_bushel = Unit(
	name='imperial bushel',
	symbols=['bsh', 'bu'],
	aliases=['bushels', 'bushel', 'imperial bushels'],
	factor='0.03636872')

# 1 imperial fluid ounce = roughly 2.84130625E-5 m^3
imperial_fluid_ounce = Unit(
	name='imperial fluid ounce',
	symbols=['fl oz', 'imp fl oz', 'impfloz'],
	aliases=['fluid ounces', 'fluid ounce', 'imperial fluid ounces'],
	factor='2.84130625E-5')

# 1 imperial gallon = roughly 0.00454609 m^3
imperial_gallon = Unit(
	name='imperial gallon',
	symbols='gal',
	aliases=['gallons', 'gallon', 'imperial gallons'],
	factor='0.00454609')

# 1 imperial pint = roughly 0.0005682615 m^3
imperial_pint = Unit(
	name='imperial pint',
	symbols=['pt'],
	aliases=['pints', 'pint', 'imperial pints'],
	factor='0.0005682615')

# 1 imperial quart = roughly 0.0011365225 m^3
imperial_quart = Unit(
	name='imperial quart',
	symbols='qt',
	aliases=['quarts', 'quart', 'imperial quarts'],
	factor='0.0011365225')

# 1 imperial tablespoon = 1.77582E-5 m^3
imperial_tablespoon = Unit(
	name='imperial tablespoon',
	symbols=['tbsp-imp', 'tbsp-uk'],
	aliases=['imperial tablespoons', 'imperial tbsp'],
	factor='1.77582E-5')

# 1 imperial teaspoon = 5.919388E-6 m^3
imperial_teaspoon = Unit(
	name='imperial teaspoon',
	symbols=['tsp-imp', 'tsp-uk'],
	aliases=['imperial teaspoons', 'imperial tsp'],
	factor='5.919388E-6')


# US customary and survey units


# 1 US gill = roughly 0.0001182941 m^3
us_gill = Unit(
	name='US gill',
	symbols='gi-us',
	aliases=['US gills', 'usgills', 'usgill'],
	factor='0.0001182941')

# 1 US cup = roughly 0.000236588 m^3
us_cup = Unit(
	name='US cup',
	aliases=['US cups', 'uscups', 'uscup'],
	factor='0.000236588')

# 1 US bushel = roughly 0.0352391 m^3
us_bushel = Unit(
	name='US bushel',
	symbols=['usbsh', 'usbu'],
	aliases='US bushels',
	factor='0.0352391')

# 1 US fluid ounce = roughly 2.95735E-5 m^3
us_fluid_ounce = Unit(
	name='US fluid ounce',
	symbols=['us fl. oz', 'us fl oz', 'usfloz'],
	aliases='US fluid ounces',
	factor='2.95735E-5')

# 1 US liquid gallon = roughly 0.003785411784 m^3
us_liquid_gallon = Unit(
	name='US liquid gallon',
	symbols=['usliquidgal', 'liquidgal', 'usgal'],
	aliases=['US liquid gallons', 'US liquid gal', 'US gal'],
	factor='0.003785411784')

# 1 US dry gallon = roughly 0.00440488 m^3
us_dry_gallon = Unit(
	name='US dry gallon',
	symbols=['usdrygal', 'drygal'],
	aliases=['US dry gallons', 'US dry gal'],
	factor='0.00440488')

# 1 US liquid pint = roughly 0.00473176 m^3
us_liquid_pint = Unit(
	name='US liquid pint',
	symbols=['usliquidpt', 'liquidpt', 'uspt'],
	aliases=['US liquid pints', 'US pints', 'US pt'],
	factor='0.000473176')

# 1 US dry pint = roughly 0.000550610475 m^3
us_dry_pint = Unit(
	name='US dry pint',
	symbols=['usdrypt', 'drypt'],
	aliases=['US dry pints', 'US dry pt'],
	factor='0.000550610475')

# 1 US liquid quart = roughly 0.000946353 m^3
us_liquid_quart = Unit(
	name='US liquid quart',
	symbols=['usliquidqt', 'liquidqt', 'usqt'],
	aliases=['US liquid quarts', 'US liquid qt', 'US quarts', 'US quart'],
	factor='0.000946353')

# 1 US dry quart = roughly 0.0011012107 m^3
us_dry_quart = Unit(
	name='US dry quart',
	symbols=['usdryqt', 'dryqt'],
	aliases=['US dry quarts', 'US dry qt'],
	factor='0.0011012107')

# 1 US tablespoon = roughly 1.47868E-5 m^3
us_tablespoon = Unit(
	name='US tablespoon',
	symbols='ustbsp',
	aliases=['US tablespoons', 'US tbsp'],
	factor='1.47868E-5')

# 1 US teaspoon = roughly 4.92892E-6 m^3
us_teaspoon = Unit(
	name='US teaspoon',
	symbols='ustsp',
	aliases=['US teaspoons', 'US tsp'],
	factor='4.92892E-6')

# 1 US survey acre-foot = roughly 1233.489238468149 m^3
us_survey_acre_foot = Unit(
	name='US survey acre-foot',
	symbols=['us ac*ft', 'usft3', 'usft^3'],
	aliases=['US survey acre-feet', 'US acre-foot', 'US acre-feet'],
	factor=area.us_survey_acre.factor * length.us_survey_foot.factor)
