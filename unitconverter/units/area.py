# Copyright (c) 2022-2023 Mike Cunningham

import unitconverter.units.length as length
from unitconverter.unit import Unit


# SI unit of area is the square metre (m^2)
square_metre = Unit(
    name='square metre',
    factor='1',
    symbols=['m^2', 'm2'],
    aliases=['square metres', 'square meters', 'square meter', 'metre^2', 'metre2'],
    power=2,
    prefix_scaling='si')

# 1 are = 100 m^2
are = Unit(
    name='are',
    factor='100.0',
    aliases='ares')

# 1 barn = 1E-28 m^2
barn = Unit(
    name='barn',
    factor='1.E-28',
    aliases='barns')

# 1 hectare = 100 ares = 100m x 100m = 10000 m^2
hectare = Unit(
    name='hectare',
    factor='10000',
    symbols='ha',
    aliases='hectares')


# Imperial units


# 1 acre is roughly 4046.8564224 m^2
acre = Unit(
    name='acre',
    factor='4046.8564224',
    symbols='ac',
    aliases=['acres', 'imperial acres', 'imperial acre'])

# 1 hide = 120 acres = 485000 m^2
hide = Unit(
    name='hide',
    factor='485000',
    aliases='hides')

# 1 rood is roughly 1011.7141056 m^2
rood = Unit(
    name='rood',
    factor='1011.7141056',
    aliases='roods')

# 1 square = 100 square feet or roughly 9.290304 m^2
square = Unit(
    name='square',
    factor='9.290304',
    aliases='Squares')

# 1 circular mil (thou) is roughly 5.067075E-10 m^2
circular_mil = Unit(
    name='circular mil',
    factor='5.06707479E-10',
    symbols=['c mil', 'c thou'],
    aliases=['circular mils', 'circular thou'])

# 1 circular inch is roughly 5.067075E-4 m^2
circular_inch = Unit(
    name='circular inch',
    factor='5.06707479E-4',
    symbols='c in',
    aliases='circular inches')

# 1 square thou (thou) is roughly 6.4516E-10 m^2
square_thou = Unit(
    name='square mil',
    factor=length.thou.factor ** 2,
    symbols=['thou^2', 'thou2', 'mil^2', 'mil2'],
    aliases=['square mils', 'square thou'])

# 1 square inch = 0.00064516 m^2
square_inch = Unit(
    name='square inch',
    factor=length.inch.factor ** 2,
    symbols=['sq in', 'sqin', 'in^2', 'in2'],
    aliases=['square inches', 'inches^2', 'inch^2'])

# 1 square foot = 0.09290304 m^2
square_foot = Unit(
    name='square foot',
    factor=length.foot.factor ** 2,
    symbols=['sq ft', 'sqft', 'ft^2', 'ft2'],
    aliases=['square feet', 'foot^2', 'feet^2'])

# 1 square yard = 0.83612736 m^2
square_yard = Unit(
    name='square yard',
    factor=length.yard.factor ** 2,
    symbols=['sq yd', 'sqyd', 'yd^2', 'yd2'],
    aliases=['square yards', 'yards^2', 'yard^2'])

# 1 square mile = 2589988.110336 m^2
square_mile = Unit(
    name='square mile',
    factor=length.mile.factor ** 2,
    symbols=['sq mi', 'sqmi', 'mi^2', 'mi2'],
    aliases=['square miles', 'miles^2', 'mile^2'])

# 1 square nautical mile = 3429904 m^2
square_nautical_mile = Unit(
    name='square nautical mile',
    factor=length.nautical_mile.factor ** 2,
    symbols=['sqnmi', 'nmi^2', 'nmi2'],
    aliases=['square nautical miles'])

# 1 square chain = 404.68564224 m^2
square_chain = Unit(
    name='square chain',
    factor=length.chain.factor ** 2,
    symbols=['sqchain', 'ch^2', 'ch2'],
    aliases=['square chains', 'chain^2', 'chain2'])

# 1 square furlong = 40468.564224 m^2
square_furlong = Unit(
    name='square furlong',
    factor=length.furlong.factor ** 2,
    symbols=['sqfur', 'fur^2', 'fur2'],
    aliases=['square furlongs', 'furlong^2', 'furlong2'])

# 1 square link = 0.040468564224 m^2
square_link = Unit(
    name='square link',
    factor=length.link.factor ** 2,
    symbols=['sqlink', 'li^2', 'li2'],
    aliases=['square links', 'link^2', 'link2'])

# 1 square rod = 25.29285264 m^2
square_rod = Unit(
    name='square rod',
    factor=length.rod.factor ** 2,
    symbols=['rod^2', 'rod2', 'pole^2', 'pole2', 'perch^2', 'perch2'],
    aliases=['square rods', 'square poles', 'square pole', 'square perch'])


# US survey units
# Source: https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors


# 1 US survey acre is 4046.872609874 m^2
us_survey_acre = Unit(
    name='US survey acre',
    factor='4046.872609874',
    symbols='ac-survey',
    aliases=['US survey acres', 'surveyacres', 'surveyacre'])

# 1 US survey square foot is roughly 0.09290341161 m^2
us_survey_square_foot = Unit(
    name='US survey square foot',
    factor=length.us_survey_foot.factor ** 2,
    symbols=['sqft-survey', 'ft^2-survey', 'ft2-survey'],
    aliases=['US survey square feet', 'surveyfoot^2', 'surveyfoot2'])

# 1 US survey square mile is roughly 2589998.47032 m^2
us_survey_square_mile = Unit(
    name='US survey square mile',
    factor=length.us_survey_mile.factor ** 2,
    symbols=['mi^2-survey', 'mi2-survey'],
    aliases=['US survey square miles', 'surveymile^2', 'surveymile2'])

# 1 US survey square rod = 25.292953807488363364 m^2
us_survey_square_rod = Unit(
    name='US survey square rod',
    factor=length.us_survey_rod.factor ** 2,
    symbols=['rd^2-survey', 'rd2-survey'],
    aliases=['US survey square rods', 'surveyrod^2', 'surveyrod2'])


# Misc.


# 1 arpent is roughly 3418.8929237 m^2
arpent = Unit(
    name='arpent',
    factor='3418.8929237',
    aliases='arpents')

# 1 homestead is roughly 647497.02758 m^2
homestead = Unit(
    name='homestead',
    factor='647497.02758',
    aliases=['survey homesteads', 'survey homestead'])

# 1 section is roughly 2589988.1103 m^2
section = Unit(
    name='section',
    factor='2589988.1103',
    aliases=['survey sections', 'survey section'])

# 1 township is roughly 93239571.972 m^2
township = Unit(
    name='township',
    factor='93239571.972',
    symbols='twp',
    aliases=['townships', 'survey townships', 'survey township'])
