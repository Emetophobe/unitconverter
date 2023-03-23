# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit
second = Unit(
    name='second',
    symbols='s',
    aliases='seconds',
    factor='1')

minute = Unit(
	name='minute',
	symbols='min',
	aliases='minutes',
	factor='60')

hour = Unit(
	name='hour',
	symbols=['hrs', 'hr'],
	aliases='hours',
	factor='3600')

day = Unit(
	name='day',
	symbols='',
	aliases='days',
	factor='86400')

week = Unit(
	name='week',
	symbols=['wks', 'wk'],
	aliases='weeks',
	factor='604800')

fortnight = Unit(
	name='fortnight',
	symbols='',
	aliases='fortnights',
	factor='1209600')

month = Unit(
	name='month',
	symbols=['mos', 'mo'],
	aliases='months',
	factor='2.628E+6')

year = Unit(
	name='year',
	symbols=['yrs', 'yr'],
	aliases='years',
	factor='3.1536E+7')

year_gregorian = Unit(
	name='gregorian year',
	symbols='',
	aliases='gregorian years',
	factor='31556952')

year_julian = Unit(
	name='julian year',
	symbols='',
	aliases='julian years',
	factor='31557600')

year_leap = Unit(
	name='leap year',
	symbols='',
	aliases='leap years',
	factor='31622400')

decade = Unit(
	name='decade',
	symbols='',
	aliases='decades',
	factor='3.1536E+8')

century = Unit(
	name='century',
	symbols='',
	aliases='centuries',
	factor='3.1536E+9')

millennia = Unit(
	name='millennia',
	symbols='',
	aliases=['millennias', 'millenniums', 'millennium'],
	factor='3.1536E+10')
