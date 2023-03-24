# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The second is the SI base unit of time
second = Unit(
    name='second',
    symbols='s',
    aliases='seconds',
    factor='1')

# 1 minute = 60 seconds
minute = Unit(
    name='minute',
    symbols='min',
    aliases='minutes',
    factor='60')

# 1 hour = 3600 seconds
hour = Unit(
    name='hour',
    symbols=['hrs', 'hr'],
    aliases='hours',
    factor='3600')

# 1 day = 86400 seconds
day = Unit(
    name='day',
    aliases='days',
    factor='86400')

# 1 week = 604800 seconds
week = Unit(
    name='week',
    symbols=['wks', 'wk'],
    aliases='weeks',
    factor='604800')

# 1 fortnight = roughly 1209600 seconds
fortnight = Unit(
    name='fortnight',
    aliases='fortnights',
    factor='1209600')

# 1 month = roughly 2.628E+6 seconds
month = Unit(
    name='month',
    symbols=['mos', 'mo'],
    aliases='months',
    factor='2.628E+6')

# 1 year = roughly 3.1536E+7 seconds
year = Unit(
    name='year',
    symbols=['yrs', 'yr'],
    aliases='years',
    factor='3.1536E+7')

# 1 gregorian year = roughly 31556952 seconds
gregorian_year = Unit(
    name='gregorian year',
    aliases='gregorian years',
    factor='31556952')

# 1 julian year = roughly 31557600 seconds
julian_year = Unit(
    name='julian year',
    aliases='julian years',
    factor='31557600')

# 1 leap year = roughly 31622400 seconds
leap_year = Unit(
    name='leap year',
    aliases='leap years',
    factor='31622400')

# 1 decade = roughly 3.1536E+8 seconds
decade = Unit(
    name='decade',
    aliases='decades',
    factor='3.1536E+8')

# 1 century = roughly 3.1536E+9 seconds
century = Unit(
    name='century',
    aliases='centuries',
    factor='3.1536E+9')

# 1 millennia = roughly 3.1536E+10 seconds
millennia = Unit(
    name='millennia',
    aliases=['millennias', 'millenniums', 'millennium'],
    factor='3.1536E+10')
