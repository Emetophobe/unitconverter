# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# 1 metre/minute (m/s) is the base unit
metre_per_second = Unit(
    name='metre per second',
    symbols='m/s',
    aliases=['metre/s', 'metres/s', 'meters/s', 'meter/s'],
    factor='1',
	prefix_index=0)

# 1 metre/minute = 1/60 = 0.0166666667 m/s
metre_per_minute = Unit(
    name='metre per minute',
    symbols='m/min',
    aliases=['metre/min', 'metres/min', 'meters/min', 'meter/min'],
    factor='0.0166666667',
	prefix_index=0)

# 1 metre/hour = 1/3600 = 0.0002777778 m/s
metre_per_hour = Unit(
    name='metre per hour',
    symbols='m/hr',
    aliases=['metres per hour', 'metres/hour', 'meter/hour'],
	factor='0.0002777778',
	prefix_index=0)

# 1 kph = 1000/3600 = 0.2777777778 m/s
# Create kph for convenience
kilometre_per_hour = Unit(
    name='kilometre per hour',
    symbols=['kph', 'km/hr'],
    aliases=['kilometres per hour', 'kilometres/hour', 'kilometer/hour'],
    factor='0.2777777778',
    prefix_scaling='none')

# 1 mph = 0.44704 m/s
mile_per_hour = Unit(
    name='mile per hour',
    symbols=['mph', 'mi/hr'],
    aliases=['miles per hour', 'miles/hour', 'mile/hour'],
    factor='0.44704',
	prefix_scaling='none')

# 1 inch/second = 0.0254 m/s
inch_per_second = Unit(
    name='inch per second',
    symbols=['in/s', 'in/sec'],
    aliases=['inches per second', 'inches/second', 'inch/second', 'inch/sec'],
    factor='0.0254',
	prefix_scaling='none')

# 1 inch/minute = 0.000423333 m/s
inch_per_minute = Unit(
    name='inch per minute',
    symbols='in/min',
    aliases=['inches per minute', 'inches/minute', 'inch/minute', 'inch/min'],
    factor='0.000423333',
	prefix_scaling='none')

# 1 inch/hour = 7.05556e-6 m/s
inch_per_hour = Unit(
    name='inch per hour',
    symbols='in/hr',
    aliases=['inches per hour', 'inches/hour', 'inch/hour', 'inch/hr'],
    factor='7.05556e-6',
	prefix_scaling='none')

# 1 foot/second = 0.3048 m/s
foot_per_second = Unit(
    name='foot per second',
    symbols=['ft/s', 'ft/sec'],
    aliases=['feet per second', 'foot/second', 'feet/second', 'foot/sec', 'feet/sec'],
    factor='0.3048',
	prefix_scaling='none')

# 1 foot/minute = 0.00508 m/s
foot_per_minute = Unit(
    name='foot per minute',
    symbols='ft/min',
    aliases=['feet per minute', 'foot/minute', 'feet/minute', 'foot/min', 'feet/min'],
    factor='0.00508',
    prefix_scaling='none')

# 1 foot/hour = 0.0000846667 m/s
foot_per_hour = Unit(
    name='foot per hour',
    symbols='ft/hr',
    aliases=['feet per hour', 'foot/hour', 'feet/hour', 'feet/hr', 'foot/hr'],
    factor='0.0000846667',
	prefix_scaling='none')

# The knot is equal to one nautical mile per hour (~0.514 m/s)
knot = Unit(
    name='knot',
    aliases='knots',
    factor='0.5144444444',
    prefix_scaling='none')

# 1 imperial knot = 0.5147733333 m/s
imperial_knot = Unit(
    name='imperial knot',
    aliases='imperial knots',
    factor='0.5147733333',
    prefix_scaling='none')

# Mach 1 (speed of sound)
mach = Unit(
    name='mach',
    symbols='Ma',
    factor='295.0464',
    prefix_scaling='none')
