# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit
meter = Unit(
    name='meter',
    symbols='m',
    aliases=['meters', 'metres', 'metre'],
    factor='1')

angstrom = Unit(
	name='angstrom',
	symbols='Å',
	aliases=['ångström', 'ångströms', 'angstroms'],
	factor='1E-10')

thou = Unit(
	name='thou',
	symbols='',
	aliases=['thousandth of an inch', 'mils', 'mil'],
	factor='2.54E-5')

barleycorn = Unit(
    name='barleycorn',
    symbols='',
    aliases='barleycorns',
    factor='0.0084667')

inch = Unit(
	name='inch',
	symbols='in',
	aliases='inches',
	factor='0.0254')

hand = Unit(
	name='hand',
	symbols='hh',
	aliases='hands',
	factor='0.1016')

foot = Unit(
	name='foot',
	symbols='ft',
	aliases='feet',
	factor='0.3048')

yard = Unit(
	name='yard',
	symbols=['yds', 'yd'],
	aliases='yards',
	factor='0.9144')

mile = Unit(
	name='mile',
	symbols='mi',
	aliases='miles',
	factor='1609.344')

# Surveying units

chain = Unit(
	name='chain',
	symbols='ch',
	aliases='chains',
	factor='20.1168')

furlong = Unit(
	name='furlong',
	symbols='fur',
	aliases='furlongs',
	factor='201.168')

link = Unit(
	name='link',
	symbols='li',
	aliases='links',
	factor='0.201168')

rod = Unit(
	name='rod',
	symbols='',
	aliases=['rods', 'perch', 'perches', 'poles', 'pole', 'lugs', 'lug'],
	factor='5.0292')

# US survey units

us_survey_link = Unit(
	name='US survey link',
	symbols='usli',
	aliases=['US survey links', 'uslinks', 'uslink'],
	factor='0.2011684023')

us_survey_chain = Unit(
	name='US survey chain',
	symbols='usch',
	aliases=['US survey chains', 'uschains', 'uschain'],
	factor='20.116840234')

us_survey_rod = Unit(
	name='US survey rod',
	symbols=['usrods', 'usrod'],
	aliases=['US survey rods', 'usperch', 'uspole', 'uslug'],
	factor='5.0292100584')

us_survey_furlong = Unit(
	name='US survey furlong',
	symbols='usfur',
	aliases=['US survey furlongs', 'usfurlongs', 'usfurlong'],
	factor='201.16840234')

us_survey_fathom = Unit(
	name='US survey fathom',
	symbols='usftm',
	aliases=['US survey fathoms', 'usfathoms', 'usfathom'],
	factor='1.8288036576')

# Nautical units

cable_length = Unit(
	name='cable length',
	symbols='cb',
	aliases=['cable lengths', 'international cable length'],
	factor='185.2')

imperial_cable_length = Unit(
	name='imperial cable length',
	symbols='impcb',
	aliases=['imperial cable lengths'],
	factor='185.32')

us_cable = Unit(
	name='US cable length',
	symbols='uscb',
	aliases=['US cable lengths'],
	factor='219.5')

fathom = Unit(
	name='fathom',
	symbols='ftm',
	aliases='fathoms',
	factor='1.8288')

league = Unit(
	name='league',
	symbols='lea',
	aliases='leagues',
	factor='4828.03')

nautical_mile = Unit(
	name='nautical mile',
	symbols=['NM', 'nmi'],
	aliases='nautical miles',
	factor='1852')

imperial_nautical_mile = Unit(
	name='imperial nautical mile',
	symbols=['imp NM', 'imp nmi'],
	aliases='imperial nautical miles',
	factor='1853.184')

# Astronomical units

planck_length = Unit(
	name='planck length',
	symbols='',
	factor='1.61605E-35')

astronomical_unit = Unit(
	name='astronomical unit',
	symbols=['AU', 'au'],
	aliases='astronomical units',
	factor='1.495978707E+11')

light_second = Unit(
	name='light second',
	symbols='ls',
	aliases=['light seconds', 'light-seconds', 'light-second'],
	factor='299792458')

light_minute = Unit(
	name='light minute',
	symbols='',
	aliases=['light minutes', 'light-minutes', 'light-minute'],
	factor='2.59020683712E+13')

light_year = Unit(
	name='light year',
	symbols='ly',
	aliases=['light years', 'light-years', 'light-year'],
	factor='9.4607E+15')

parsec = Unit(
	name='parsec',
	symbols='pc',
	aliases='parsecs',
	factor='3.0857E+16')

# Typesetting units

twip = Unit(
	name='twip',
	symbols='',
	aliases='twips',
	factor='0.0000176389')

point = Unit(
	name='point',
	symbols='',
	aliases='points',
	factor='0.0003527778')

# Misc

caliber = Unit(
	name='caliber',
	symbols='',
	aliases='calibre',
	factor='0.000254')
