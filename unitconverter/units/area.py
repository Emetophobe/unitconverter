# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of area is the square meter (meter^2)
square_meter = Unit(
	name='square meter',
	symbols=['sqm', 'm^2', 'm2'],
	aliases=['square meters', 'square metres', 'square metre', 'meter^2', 'meter2'],
	factor='1',
	power=2)

are = Unit(
	name='are',
	aliases='ares',
	factor='100.0')

acre = Unit(
	name='acre',
	symbols='ac',
	aliases=['acres', 'imperial acres', 'imperial acre'],
	factor='4046.8564224')

barn = Unit(
	name='barn',
	aliases='barns',
	factor='1.E-28')

hectare = Unit(
	name='hectare',
	symbols='ha',
	aliases='hectares',
	factor='10000.0')

circular_mil = Unit(
	name='circular mil',
	symbols=['c mil', 'c thou'],
	aliases=['circular mils', 'circular thou'],
	factor='5.06707479E-10')

circular_inch = Unit(
	name='circular inch',
	symbols='c in',
	aliases='circular inches',
	factor='0.000506707479')

square_mil = Unit(
	name='square mil',
	symbols=['thou^2', 'thou2', 'mil^2', 'mil2'],
	aliases=['square mils', 'square thou'],
	factor='6.4516E-10')

square_inch = Unit(
	name='square inch',
	symbols=['sq in', 'sqin', 'in^2', 'in2'],
	aliases=['square inches', 'inches^2', 'inch^2'],
	factor='0.00064516')

square_foot = Unit(
	name='square foot',
	symbols=['sq ft', 'sqft', 'ft^2', 'ft2'],
	aliases=['square feet', 'foot^2', 'feet^2'],
	factor='0.09290304')

square_yard = Unit(
	name='square yard',
	symbols=['sq yd', 'sqyd', 'yd^2', 'yd2'],
	aliases=['square yards', 'yards^2', 'yard^2'],
	factor='0.83612736')

square_mile = Unit(
	name='square mile',
	symbols=['sq mi', 'sqmi', 'mi^2', 'mi2'],
	aliases=['square miles', 'miles^2', 'mile^2'],
	factor='2589988.110336')

square_nautical_mile = Unit(
	name='square nautical mile',
	symbols=['sqnmi', 'nmi^2', 'nmi2'],
	aliases=['square nautical miles'],
	factor='3.43E+6')

square_chain = Unit(
	name='square chain',
	symbols=['sqchain', 'chain^2', 'chain2', 'ch^2', 'ch2'],
	aliases='square chains',
	factor='404.68564224')

square_rod = Unit(
	name='square rod',
	symbols=['sqrod', 'pole^2', 'pole2', 'rod^2', 'rod2'],
	aliases=['square rods', 'square poles', 'square pole', 'square perch', 'sq rod'],
	factor='25.29285264')

# US survey units

us_survey_acre = Unit(
	name='US survey acre',
	symbols='usac',
	aliases=['US survey acres', 'surveyacres', 'surveyacre'],
	factor='4046.87')

us_survey_square_foot = Unit(
	name='US survey square foot',
	symbols=['ussqft', 'usft^2', 'usft2'],
	aliases=['US survey square feet', 'surveyfoot^2', 'surveyfoot2'],
	factor='0.092903411613')

us_survey_square_mile = Unit(
	name='US survey square mile',
	symbols=['usmi^2', 'usmi2'],
	aliases=['US survey square miles', 'surveymile^2', 'surveymile2'],
	factor='2589998.4703')

us_survey_square_rod = Unit(
	name='US survey square rod',
	symbols=['usrod^2', 'usrod2'],
	aliases=['US survey square rods', 'surveyrod^2', 'surveyrod2'],
	factor='25.29285264')

# Misc

arpent = Unit(
	name='arpent',
	aliases='arpents',
	factor='3418.8929237')

hide = Unit(
	name='hide',
	aliases='hides',
	factor='485000.0')

rood = Unit(
	name='rood',
	aliases='roods',
	factor='1011.7141056')

square = Unit(
	name='square',
	aliases='Squares',
	factor='9.290304')

township = Unit(
	name='township',
	symbols='twp',
	aliases=['townships', 'survey townships', 'survey township'],
	factor='93239571.972')

homestead = Unit(
	name='homestead',
	aliases=['survey homesteads', 'survey homestead'],
	factor='647497.02758')

section = Unit(
	name='section',
	aliases=['survey sections', 'survey section'],
	factor='2589988.1103')
