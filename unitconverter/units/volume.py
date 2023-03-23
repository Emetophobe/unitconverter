# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of volume (meter^3)
cubic_meter = Unit(
	name='cubic meter',
	symbols=['m^3', 'm3'],
	aliases=['cubic meters', 'cubic metres', 'cubic metre', 'meter^3', 'meter3'],
	factor='1',
	power=3)

liter = Unit(
	name='liter',
	symbols=['L', 'l'],
	aliases=['liters', 'litres', 'litre'],
	factor='1E-3')

cubic_inch = Unit(
	name='cubic inch',
	symbols=['cu in', 'in^3', 'in3'],
	aliases='cubic inches',
	factor='1.63871E-5')

cubic_foot = Unit(
	name='cubic foot',
	symbols=['cu ft', 'ft^3', 'ft3'],
	aliases='cubic feet',
	factor='0.0283168')

cubic_yard = Unit(
	name='cubic yard',
	symbols=['cu yd', 'yd^3', 'yd3'],
	aliases='cubic yards',
	factor='0.764555')

cubic_mile = Unit(
	name='cubic mile',
	symbols=['cu mi', 'mi^3', 'mi3'],
	aliases='cubic miles',
	factor='4.168E+9')

acre_inch = Unit(
	name='acre-inch',
	symbols=['ac*in', 'acin'],
	aliases=['acre-inches', 'acre-in'],
	factor='102.79015313')

acre_foot = Unit(
	name='acre-foot',
	symbols=['ac*ft', 'acft'],
	aliases='acre-feet',
	factor='1233.4818375')

cup = Unit(
	name='cup',
	aliases=['cups', 'metric cups', 'metric cup'],
	factor='0.00025')

tablespoon = Unit(
	name='tablespoon',
	symbols='tbsp',
	aliases=['tablespoons', 'metric tablespoons', 'metric tablespoon'],
	factor='1.5E-5')

teaspoon = Unit(
	name='teaspoon',
	symbols='tsp',
	aliases=['teaspoons', 'metric teaspoons', 'metric teaspoon'],
	factor='5E-6')

stere = Unit(
	name='stere',
	aliases=['steres', 'stères', 'stère'],
	factor='1')

drop = Unit(
	name='drop',
	symbols='gt',
	aliases='drops',
	factor='5E-8')

# Imperial units

imperial_gill = Unit(
	name='imperial gill',
	symbols='gi',
	aliases=['gills', 'gill', 'imperial gills'],
	factor='0.0001420653')

imperial_cup = Unit(
	name='imperial cup',
	aliases=['imperial cups', 'impcups', 'impcup'],
	factor='0.0002841306')

imperial_bushel = Unit(
	name='imperial bushel',
	symbols=['bsh', 'bu'],
	aliases=['bushels', 'bushel', 'imperial bushels'],
	factor='0.0363687')

imperial_fluid_ounce = Unit(
	name='imperial fluid ounce',
	symbols=['fl oz', 'imp fl oz', 'impfloz'],
	aliases=['fluid ounces', 'fluid ounce', 'imperial fluid ounces'],
	factor='2.84131E-5')

imperial_gallon = Unit(
	name='imperial gallon',
	symbols='gal',
	aliases=['gallons', 'gallon', 'imperial gallons'],
	factor='0.00454609')

imperial_pint = Unit(
	name='imperial pint',
	symbols=['pt'],
	aliases=['pints', 'pint', 'imperial pints'],
	factor='0.000568261')

imperial_quart = Unit(
	name='imperial quart',
	symbols='qt',
	aliases=['quarts', 'quart', 'imperial quarts'],
	factor='0.0011365225')

imperial_tablespoon = Unit(
	name='imperial tablespoon',
	symbols=['imptbsp', 'uktbsp'],
	aliases=['imperial tablespoons', 'imperial tbsp'],
	factor='1.77582E-5')

imperial_teaspoon = Unit(
	name='imperial teaspoon',
	symbols=['imptsp', 'uktsp'],
	aliases=['imperial teaspoons', 'imperial tsp'],
	factor='5.919388E-6')

# US customary and survey units

us_gill = Unit(
	name='US gill',
	symbols='usgi',
	aliases=['US gills', 'usgills', 'usgill'],
	factor='0.0001182941')

us_cup = Unit(
	name='US cup',
	aliases=['US cups', 'uscups', 'uscup'],
	factor='0.000236588')

us_bushel = Unit(
	name='US bushel',
	symbols=['usbsh', 'usbu'],
	aliases='US bushels',
	factor='0.0352391')

us_fluid_ounce = Unit(
	name='US fluid ounce',
	symbols=['us fl. oz', 'us fl oz', 'usfloz'],
	aliases='US fluid ounces',
	factor='2.95735E-5')

us_liquid_gallon = Unit(
	name='US liquid gallon',
	symbols=['usliquidgal', 'liquidgal', 'usgal'],
	aliases=['US liquid gallons', 'US liquid gal', 'US gal'],
	factor='0.003785411784')

us_dry_gallon = Unit(
	name='US dry gallon',
	symbols=['usdrygal', 'drygal'],
	aliases=['US dry gallons', 'US dry gal'],
	factor='0.00440488')

us_liquid_pint = Unit(
	name='US liquid pint',
	symbols=['usliquidpt', 'liquidpt', 'uspt'],
	aliases=['US liquid pints', 'US pints', 'US pt'],
	factor='0.000473176')

us_dry_pint = Unit(
	name='US dry pint',
	symbols=['usdrypt', 'drypt'],
	aliases=['US dry pints', 'US dry pt'],
	factor='0.000550610475')

us_liquid_quart = Unit(
	name='US liquid quart',
	symbols=['usliquidqt', 'liquidqt', 'usqt'],
	aliases=['US liquid quarts', 'US liquid qt', 'US quarts', 'US quart'],
	factor='0.000946353')

us_dry_quart = Unit(
	name='US dry quart',
	symbols=['usdryqt', 'dryqt'],
	aliases=['US dry quarts', 'US dry qt'],
	factor='0.001101221')

us_tablespoon = Unit(
	name='US tablespoon',
	symbols='ustbsp',
	aliases=['US tablespoons', 'US tbsp'],
	factor='1.47868E-5')

us_teaspoon = Unit(
	name='US teaspoon',
	symbols='ustsp',
	aliases=['US teaspoons', 'US tsp'],
	factor='4.9289216145833E-6')

# US survey units

us_survey_acre_foot = Unit(
	name='US survey acre-foot',
	symbols=['us ac*ft', 'usft3', 'usft^3'],
	aliases=['US survey acre-feet', 'US acre-foot', 'US acre-feet'],
	factor='1233.4892385')
