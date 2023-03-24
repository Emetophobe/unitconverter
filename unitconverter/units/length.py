# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The meter is the SI base unit of length
meter = Unit(
	name='meter',
	symbols='m',
	aliases=['meters', 'metres', 'metre'],
	factor='1')

# 1 angstrom = 1E-10 meters
angstrom = Unit(
	name='angstrom',
	symbols='Å',
	aliases=['ångström', 'ångströms', 'angstroms'],
	factor='1E-10')

# 1 thousands of an itch = 2.54E-5 meters
thou = Unit(
	name='thou',
	aliases=['thousandth of an inch', 'mils', 'mil'],
	factor='2.54E-5')

# 1 inch = 0.0254 meters
inch = Unit(
	name='inch',
	symbols='in',
	aliases='inches',
	factor='0.0254')

# 1 hand = 0.1016 meters
hand = Unit(
	name='hand',
	symbols='hh',
	aliases='hands',
	factor='0.1016')

# 1 foot = 0.3048 meters
foot = Unit(
	name='foot',
	symbols='ft',
	aliases='feet',
	factor='0.3048')

# 1 yard = 0.9144 meters
yard = Unit(
	name='yard',
	symbols=['yds', 'yd'],
	aliases='yards',
	factor='0.9144')

# 1 mile = 1609.344 meters
mile = Unit(
	name='mile',
	symbols='mi',
	aliases='miles',
	factor='1609.344')

# 1 chain = 20.1168 meters
chain = Unit(
	name='chain',
	symbols='ch',
	aliases='chains',
	factor='20.1168')

# 1 furlong = 10 chain = 40 rod = 201.168 meters
furlong = Unit(
	name='furlong',
	symbols='fur',
	aliases='furlongs',
	factor='201.168')

# 1 link = 0.01 chain = 0.201168 meters
link = Unit(
	name='link',
	symbols='li',
	aliases='links',
	factor='0.201168')

# 1 rod = 0.25 chain = 5.0292 meters
rod = Unit(
	name='rod',
	symbols='rd',
	aliases=['rods', 'perch', 'poles', 'pole', 'lugs', 'lug'],
	factor='5.0292')


# US Survey units
# Source: https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors


# 1 US Survey foot = 0.304800609601 meters
us_survey_foot = Unit(
	name='US survey foot',
	symbols='ft-survey',
	aliases=['US survey feet', 'surveyfoot', 'surveyfeet'],
	factor='0.304800609601')

# 1 US survey cable length = 120 fathoms or 219.456438913 meters
us_survey_cable_length = Unit(
	name='US survey cable length',
	aliases=['surveycables', 'surveycable'],
	factor='219.456438913')

# 1 US survey chain = 20.116840234 meters
us_survey_chain = Unit(
	name='US survey chain',
	symbols='ch-survey',
	aliases=['US survey chains', 'surveychains', 'surveychain'],
	factor='20.116840234')

# 1 US survey fathom = 1.828803658 meters
us_survey_fathom = Unit(
	name='US survey fathom',
	symbols='ftm-survey',
	aliases=['US survey fathoms', 'surveyfathoms', 'surveyfathom'],
	factor='1.828803658')

# 1 US survey furlong = 201.168402337 meters
us_survey_furlong = Unit(
	name='US survey furlong',
	symbols='fur-survey',
	aliases=['US survey furlongs', 'surveyfurlongs', 'surveyfurlong'],
	factor='201.168402337')

# 1 US survey league = 4828.041656083 meters
us_survey_league = Unit(
	name='US survey league',
	symbols='lea-survey',
	aliases=['US survey leagues', 'surveyleagues', 'surveyleague'],
	factor='4828.041656083')

# 1 US survey link = 0.201168402 meters
us_survey_link = Unit(
	name='US survey link',
	symbols='li-survey',
	aliases=['US survey links', 'surveylinks', 'surveylink'],
	factor='0.201168402')

# 1 US survey mile = 1609.347218694 meters
us_survey_mile = Unit(
	name='US survey mile',
	symbols='mi-survey',
	aliases=['US survey miles', 'surveymiles', 'surveymile'],
	factor='1609.347218694')

# 1 US survey rod = 5.029210058 meters
us_survey_rod = Unit(
	name='US survey rod',
	symbols='rod-survey',
	aliases=['US survey rods', 'surveyrods', 'surveyrod', 'surveyperch', 'surveypole'],
	factor='5.029210058')


# Nautical units


# 1 international cable length = 185.2 meters
cable_length = Unit(
	name='cable length',
	symbols='cb',
	aliases=['cable lengths', 'international cable length'],
	factor='185.2')

# 1 imperial cable length = 185.32 meters
imperial_cable_length = Unit(
	name='imperial cable length',
	symbols=['cb-imp', 'cb-uk'],
	aliases=['imperial cable lengths'],
	factor='185.32')

# 1 US cable length = 219.456 meters
us_cable_length = Unit(
	name='US cable length',
	symbols='cb-us',
	aliases=['US cable lengths'],
	factor='219.456')

# 1 fathom = 1.8288 meters
fathom = Unit(
	name='fathom',
	symbols='ftm',
	aliases='fathoms',
	factor='1.8288')

# 1 league = 4828.032 meters
league = Unit(
	name='league',
	symbols='lea',
	aliases='leagues',
	factor='4828.032')

# 1 nautical mile = 1852 meters
nautical_mile = Unit(
	name='nautical mile',
	symbols=['NM', 'nmi'],
	aliases='nautical miles',
	factor='1852')

# 1 imperial nautical mile = 1583.184 meters
imperial_nautical_mile = Unit(
	name='imperial nautical mile',
	symbols=['NM-imp', 'nmi-imp'],
	aliases='imperial nautical miles',
	factor='1853.184')


# Astronomical units


# 1 planck length = 1.61605E-35 meters
planck_length = Unit(
	name='planck length',
	factor='1.61605E-35')

# 1 astronomical unit  = 1.495978707E+11 meters
astronomical_unit = Unit(
	name='astronomical unit',
	symbols=['AU', 'au'],
	aliases='astronomical units',
	factor='1.495978707E+11')

# 1 light second = 299,792,458 meters
light_second = Unit(
	name='light second',
	symbols='ls',
	aliases=['light seconds', 'light-seconds', 'light-second'],
	factor='299792458')

# 1 light minute = 1.798754748E+10 meters
light_minute = Unit(
	name='light minute',
	aliases=['light minutes', 'light-minutes', 'light-minute'],
	factor='1.798754748E+10')

# 1 light year = 9.46073047E+15 meters
light_year = Unit(
	name='light year',
	symbols='ly',
	aliases=['light years', 'light-years', 'light-year'],
	factor='9.46073047E+15')

# 1 parsec = 3.0857E+16 meters
parsec = Unit(
	name='parsec',
	symbols='pc',
	aliases='parsecs',
	factor='3.0857E+16')


# Typesetting units


# 1 twip = 1 twentieth of a point = 0.0000176389 meters
twip = Unit(
	name='twip',
	aliases='twips',
	factor='0.0000176389')

# 1 point = 0.000352778 meters
point = Unit(
	name='point',
	aliases='points',
	factor='0.000352778')


# Misc


# 1 barleycorn is roughly 0.00846667 meters
barleycorn = Unit(
	name='barleycorn',
	aliases='barleycorns',
	factor='0.0084667')

# 1 caliber is roughly 0.000254 meters
caliber = Unit(
	name='caliber',
	aliases='calibre',
	factor='0.000254')
