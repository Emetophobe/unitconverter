# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class Time(Unit):
    category = 'time'


# The second is the SI base unit of time
second = Time(
    name='second',
    factor='1',
    symbols='s',
    aliases=['seconds', 'sec'],
    prefix_scaling='si')

# 1 minute = 60 seconds
minute = Time(
    name='minute',
    factor='60',
    symbols='min',
    aliases='minutes')

# 1 hour = 3600 seconds
hour = Time(
    name='hour',
    factor='3600',
    symbols=['hrs', 'hr', 'h'],
    aliases='hours')

# 1 day = 86400 seconds
day = Time(
    name='day',
    factor='86400',
    aliases='days')

# 1 week = 604800 seconds
week = Time(
    name='week',
    factor='604800',
    symbols=['wks', 'wk'],
    aliases='weeks')

# 1 fortnight = roughly 1209600 seconds
fortnight = Time(
    name='fortnight',
    factor='1209600',
    aliases='fortnights')

# 1 month = roughly 2.628E+6 seconds
month = Time(
    name='month',
    factor='2.628E+6',
    symbols=['mos', 'mo'],
    aliases='months')

# 1 year = roughly 3.1536E+7 seconds
year = Time(
    name='year',
    factor='3.1536E+7',
    symbols=['yrs', 'yr'],
    aliases='years')

# 1 gregorian year = roughly 31556952 seconds
gregorian_year = Time(
    name='gregorian year',
    factor='31556952',
    aliases='gregorian years')

# 1 julian year = roughly 31557600 seconds
julian_year = Time(
    name='julian year',
    factor='31557600',
    aliases='julian years')

# 1 leap year = roughly 31622400 seconds
leap_year = Time(
    name='leap year',
    factor='31622400',
    aliases='leap years')

# 1 decade = roughly 3.1536E+8 seconds
decade = Time(
    name='decade',
    factor='3.1536E+8',
    aliases='decades')

# 1 century = roughly 3.1536E+9 seconds
century = Time(
    name='century',
    factor='3.1536E+9',
    aliases='centuries')

# 1 millennia = roughly 3.1536E+10 seconds
millennia = Time(
    name='millennia',
    factor='3.1536E+10',
    aliases=['millennias', 'millenniums', 'millennium'])
