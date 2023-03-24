# Copyright (c) 2022-2023 Mike Cunningham

import unitconverter.units.length as length
from unitconverter.unit import Unit


# SI unit of area is the square meter (m^2)
square_meter = Unit(
	name='square meter',
	symbols=['sqm', 'm^2', 'm2'],
	aliases=['square meters', 'square metres', 'square metre', 'meter^2', 'meter2'],
	factor='1',
	power=2)

# 1 are = 100 m^2
are = Unit(
	name='are',
	aliases='ares',
	factor='100.0')

# 1 acre is roughly 4046.8564224 m^2
acre = Unit(
	name='acre',
	symbols='ac',
	aliases=['acres', 'imperial acres', 'imperial acre'],
	factor='4046.8564224')

# 1 barn = 1E-28 m^2
barn = Unit(
	name='barn',
	aliases='barns',
	factor='1.E-28')

# 1 hectare = 10000 m^2
hectare = Unit(
	name='hectare',
	symbols='ha',
	aliases='hectares',
	factor='10000')

# 1 circular mil (thou) is roughly 5.067075E-10 m^2
circular_mil = Unit(
	name='circular mil',
	symbols=['c mil', 'c thou'],
	aliases=['circular mils', 'circular thou'],
	factor='5.06707479E-10')

# 1 circular inch is roughly 5.067075E-4 m^2
circular_inch = Unit(
	name='circular inch',
	symbols='c in',
	aliases='circular inches',
	factor='5.06707479E-4')

# 1 square thou (thou) is roughly 6.4516E-10 m^2
square_thou = Unit(
	name='square mil',
	symbols=['thou^2', 'thou2', 'mil^2', 'mil2'],
	aliases=['square mils', 'square thou'],
	factor=length.thou.factor ** 2)

# 1 square inch = 0.00064516 m^2
square_inch = Unit(
	name='square inch',
	symbols=['sq in', 'sqin', 'in^2', 'in2'],
	aliases=['square inches', 'inches^2', 'inch^2'],
	factor=length.inch.factor ** 2)

# 1 square foot = 0.09290304 m^2
square_foot = Unit(
	name='square foot',
	symbols=['sq ft', 'sqft', 'ft^2', 'ft2'],
	aliases=['square feet', 'foot^2', 'feet^2'],
	factor=length.foot.factor ** 2)

# 1 square yard = 0.83612736 m^2
square_yard = Unit(
	name='square yard',
	symbols=['sq yd', 'sqyd', 'yd^2', 'yd2'],
	aliases=['square yards', 'yards^2', 'yard^2'],
	factor=length.yard.factor ** 2)

# 1 square mile = 2589988.110336 m^2
square_mile = Unit(
	name='square mile',
	symbols=['sq mi', 'sqmi', 'mi^2', 'mi2'],
	aliases=['square miles', 'miles^2', 'mile^2'],
	factor=length.mile.factor ** 2)

# 1 square nautical mile = 3429904 m^2
square_nautical_mile = Unit(
	name='square nautical mile',
	symbols=['sqnmi', 'nmi^2', 'nmi2'],
	aliases=['square nautical miles'],
	factor=length.nautical_mile.factor ** 2)

# 1 square chain = 404.68564224 m^2
square_chain = Unit(
	name='square chain',
	symbols=['sqchain', 'ch^2', 'ch2'],
	aliases=['square chains', 'chain^2', 'chain2'],
	factor=length.chain.factor ** 2)

# 1 square furlong = 40468.564224 m^2
square_furlong = Unit(
	name='square furlong',
	symbols=['sqfur', 'fur^2', 'fur2'],
	aliases=['square furlongs', 'furlong^2', 'furlong2'],
	factor=length.furlong.factor ** 2)

# 1 square link = 0.040468564224 m^2
square_link = Unit(
	name='square link',
	symbols=['sqlink', 'li^2', 'li2'],
	aliases=['square links', 'link^2', 'link2'],
	factor=length.link.factor ** 2)

# 1 square rod = 25.29285264 m^2
square_rod = Unit(
	name='square rod',
	symbols=['sqrod', 'pole^2', 'pole2', 'rod^2', 'rod2'],
	aliases=['square rods', 'square poles', 'square pole', 'square perch', 'sq rod'],
	factor=length.rod.factor ** 2)


# US survey units
# Source: https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors


# 1 US survey acre is 4046.872609874 m^2
us_survey_acre = Unit(
	name='US survey acre',
	symbols='ac-survey',
	aliases=['US survey acres', 'surveyacres', 'surveyacre'],
	factor='4046.872609874')

# 1 US survey square foot is roughly 0.09290341161 m^2
us_survey_square_foot = Unit(
	name='US survey square foot',
	symbols=['sqft-survey', 'ft^2-survey', 'ft2-survey'],
	aliases=['US survey square feet', 'surveyfoot^2', 'surveyfoot2'],
	factor=length.us_survey_foot.factor ** 2)

# 1 US survey square mile is roughly 2589998.47032 m^2
us_survey_square_mile = Unit(
	name='US survey square mile',
	symbols=['mi^2-survey', 'mi2-survey'],
	aliases=['US survey square miles', 'surveymile^2', 'surveymile2'],
	factor=length.us_survey_mile.factor ** 2)

# 1 US survey square rod = 25.292953807488363364 m^2
us_survey_square_rod = Unit(
	name='US survey square rod',
	symbols=['rd^2-survey', 'rd2-survey'],
	aliases=['US survey square rods', 'surveyrod^2', 'surveyrod2'],
	factor=length.us_survey_rod.factor ** 2)


# Misc.


# 1 arpent is roughly 3418.8929237 m^2
arpent = Unit(
	name='arpent',
	aliases='arpents',
	factor='3418.8929237')

# 1 hide = 485000 m^2
hide = Unit(
	name='hide',
	aliases='hides',
	factor='485000')

# 1 rood is roughly 1011.7141056 m^2
rood = Unit(
	name='rood',
	aliases='roods',
	factor='1011.7141056')

# 1 square is roughly 9.290304 m^2
square = Unit(
	name='square',
	aliases='Squares',
	factor='9.290304')

# 1 township is roughly 93239571.972 m^2
township = Unit(
	name='township',
	symbols='twp',
	aliases=['townships', 'survey townships', 'survey township'],
	factor='93239571.972')

# 1 homestead is roughly 647497.02758 m^2
homestead = Unit(
	name='homestead',
	aliases=['survey homesteads', 'survey homestead'],
	factor='647497.02758')

# 1 section is roughly 2589988.1103 m^2
section = Unit(
	name='section',
	aliases=['survey sections', 'survey section'],
	factor='2589988.1103')
