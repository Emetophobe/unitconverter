# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The metre is the SI base unit of length
metre = Unit(
    name='metre',
    factor='1',
    symbols='m',
    aliases=['metres', 'meters', 'meter'],
    prefix_scaling='si')


# Create alias for American spelling of meter
meter = metre


# 1 angstrom = 1E-10 metres (0.1 nanometers)
angstrom = Unit(
    name='angstrom',
    factor='1E-10',
    symbols='Å',
    aliases=['angstroms', 'ångström', 'ångströms'])

# 1 thousands of an itch = 2.54E-5 metres
thou = Unit(
    name='thou',
    factor='2.54E-5',
    aliases=['thousandth of an inch', 'mils', 'mil'])

# 1 inch = 0.0254 metres
inch = Unit(
    name='inch',
    factor='0.0254',
    symbols='in',
    aliases='inches')

# 1 hand = 0.1016 metres
hand = Unit(
    name='hand',
    factor='0.1016',
    symbols='hh',
    aliases='hands')

# 1 foot = 0.3048 metres
foot = Unit(
    name='foot',
    factor='0.3048',
    symbols='ft',
    aliases='feet')

# 1 yard = 0.9144 metres
yard = Unit(
    name='yard',
    factor='0.9144',
    symbols=['yds', 'yd'],
    aliases='yards')

# 1 mile = 1609.344 metres
mile = Unit(
    name='mile',
    factor='1609.344',
    symbols='mi',
    aliases='miles')

# 1 chain = 20.1168 metres
chain = Unit(
    name='chain',
    factor='20.1168',
    symbols='ch',
    aliases='chains')

# 1 furlong = 10 chain = 40 rod = 201.168 metres
furlong = Unit(
    name='furlong',
    factor='201.168',
    symbols='fur',
    aliases='furlongs')

# 1 link = 0.01 chain = 0.201168 metres
link = Unit(
    name='link',
    factor='0.201168',
    symbols='li',
    aliases='links')

# 1 rod = 0.25 chain = 5.0292 metres
rod = Unit(
    name='rod',
    factor='5.0292',
    symbols='rd',
    aliases=['rods', 'perch', 'poles', 'pole', 'lugs', 'lug'])


# US Survey units
# Source: https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors


# 1 US Survey foot = 0.304800609601 metres
us_survey_foot = Unit(
    name='US survey foot',
    factor='0.304800609601',
    symbols='ft-survey',
    aliases=['US survey feet', 'surveyfoot', 'surveyfeet'])

# 1 US survey cable length = 120 fathoms or 219.456438913 metres
us_survey_cable_length = Unit(
    name='US survey cable length',
    factor='219.456438913',
    aliases=['US survey cable', 'surveycables', 'surveycable'])

# 1 US survey chain = 20.116840234 metres
us_survey_chain = Unit(
    name='US survey chain',
    factor='20.116840234',
    symbols='ch-survey',
    aliases=['US survey chains', 'surveychains', 'surveychain'])

# 1 US survey fathom = 1.828803658 metres
us_survey_fathom = Unit(
    name='US survey fathom',
    factor='1.828803658',
    symbols='ftm-survey',
    aliases=['US survey fathoms', 'surveyfathoms', 'surveyfathom'])

# 1 US survey furlong = 201.168402337 metres
us_survey_furlong = Unit(
    name='US survey furlong',
    factor='201.168402337',
    symbols='fur-survey',
    aliases=['US survey furlongs', 'surveyfurlongs', 'surveyfurlong'])

# 1 US survey league = 4828.041656083 metres
us_survey_league = Unit(
    name='US survey league',
    factor='4828.041656083',
    symbols='lea-survey',
    aliases=['US survey leagues', 'surveyleagues', 'surveyleague'])

# 1 US survey link = 0.201168402 metres
us_survey_link = Unit(
    name='US survey link',
    factor='0.201168402',
    symbols='li-survey',
    aliases=['US survey links', 'surveylinks', 'surveylink'])

# 1 US survey mile = 1609.347218694 metres
us_survey_mile = Unit(
    name='US survey mile',
    factor='1609.347218694',
    symbols='mi-survey',
    aliases=['US survey miles', 'surveymiles', 'surveymile'])

# 1 US survey rod = 5.029210058 metres
us_survey_rod = Unit(
    name='US survey rod',
    factor='5.029210058',
    symbols='rod-survey',
    aliases=['US survey rods', 'surveyrods', 'surveyrod', 'surveyperch', 'surveypole'])


# Nautical units


# 1 international cable length = 185.2 metres
cable_length = Unit(
    name='cable length',
    factor='185.2',
    symbols='cb',
    aliases=['cable lengths', 'international cable length'])

# 1 imperial cable length = 185.32 metres
imperial_cable_length = Unit(
    name='imperial cable length',
    factor='185.32',
    symbols=['cb-imp', 'cb-uk'],
    aliases=['imperial cable lengths'])

# 1 US cable length = 219.456 metres
us_cable_length = Unit(
    name='US cable length',
    factor='219.456',
    symbols='cb-us',
    aliases=['US cable lengths'])

# 1 fathom = 1.8288 metres
fathom = Unit(
    name='fathom',
    factor='1.8288',
    symbols='ftm',
    aliases='fathoms')

# 1 league = 4828.032 metres
league = Unit(
    name='league',
    factor='4828.032',
    symbols='lea',
    aliases='leagues')

# 1 nautical mile = 1852 metres
nautical_mile = Unit(
    name='nautical mile',
    factor='1852',
    symbols=['NM', 'nmi'],
    aliases='nautical miles')

# 1 imperial nautical mile = 1583.184 metres
imperial_nautical_mile = Unit(
    name='imperial nautical mile',
    factor='1853.184',
    symbols=['NM-imp', 'nmi-imp'],
    aliases='imperial nautical miles')


# Astronomical units


# 1 planck length = 1.61605E-35 metres
planck_length = Unit(
    name='planck length',
    factor='1.61605E-35')

# 1 astronomical unit  = 1.495978707E+11 metres
astronomical_unit = Unit(
    name='astronomical unit',
    factor='1.495978707E+11',
    symbols=['AU', 'au'],
    aliases='astronomical units')

# 1 light second = 299,792,458 metres
light_second = Unit(
    name='light second',
    factor='299792458',
    symbols='ls',
    aliases=['light seconds', 'light-seconds', 'light-second'])

# 1 light minute = 1.798754748E+10 metres
light_minute = Unit(
    name='light minute',
    factor='1.798754748E+10',
    aliases=['light minutes', 'light-minutes', 'light-minute'])

# 1 light year = 9.46073047E+15 metres
light_year = Unit(
    name='light year',
    factor='9.46073047E+15',
    symbols='ly',
    aliases=['light years', 'light-years', 'light-year'])

# 1 parsec = 3.0857E+16 metres
parsec = Unit(
    name='parsec',
    factor='3.0857E+16',
    symbols='pc',
    aliases='parsecs')


# Typesetting units


# 1 twip = 1 twentieth of a point = 0.0000176389 metres
twip = Unit(
    name='twip',
    factor='0.0000176389',
    aliases='twips')

# 1 point = 0.000352778 metres
point = Unit(
    name='point',
    factor='0.000352778',
    aliases='points')


# Misc


# 1 barleycorn is roughly 0.00846667 metres
barleycorn = Unit(
    name='barleycorn',
    factor='0.0084667',
    aliases='barleycorns')

# 1 caliber is roughly 0.000254 metres
caliber = Unit(
    name='caliber',
    factor='0.000254',
    aliases='calibre')
