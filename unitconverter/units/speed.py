# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


meter_per_second = Unit(
	name='meter per second',
	symbols='m/s',
	aliases=['meters per second', 'metres per second', 'metre per second'],
	factor='1')

meter_per_minute = Unit(
	name='meter per minute',
	symbols='m/min',
	aliases=['meters per minute', 'metres per minute', 'metre per minute'],
	factor='0.0166666667')

meter_per_hour = Unit(
	name='meter per hour',
	symbols='m/hr',
	aliases=['meters per hour', 'metres per hour', 'metre per hour'],
	factor='0.0002777778')

kilometer_per_hour = Unit(
	name='kilometer per hour',
	symbols=['kph', 'km/hr'],
	aliases=['kilometers per hour', 'km/hour'],
	factor='0.2777777778',
	scaling='none')

mile_per_hour = Unit(
	name='mile per hour',
	symbols=['mph', 'mi/hr'],
	aliases='miles per hour',
	factor='0.44704')

inch_per_second = Unit(
	name='inch per second',
	symbols=['in/s', 'in/sec'],
	aliases='inches per second',
	factor='0.0254')

inch_per_minute = Unit(
	name='inch per minute',
	symbols='in/min',
	aliases='inches per minute',
	factor='0.000423333')

inch_per_hour = Unit(
	name='inch per hour',
	symbols='in/hr',
	aliases='inches per hour',
	factor='7.05556e-6')

foot_per_second = Unit(
	name='foot per second',
	symbols=['ft/s', 'ft/sec'],
	aliases='feet per second',
	factor='0.3048')

foot_per_minute = Unit(
	name='foot per minute',
	symbols='ft/min',
	aliases='feet per minute',
	factor='0.00508')

foot_per_hour = Unit(
	name='foot per hour',
	symbols='ft/hr',
	aliases='feet per hour',
	factor='0.0000846667')

# The knot is equal to one nautical mile per hour (1.852 km/h or 0.514 m/s)
knot = Unit(
	name='knot',
	symbols='',
	aliases='knots',
	factor='0.5144444444')

imperial_knot = Unit(
	name='imperial knot',
	symbols='',
	aliases='imperial knots',
	factor='0.5147733333')

# Mach 1
mach = Unit(
	name='mach',
	symbols='Ma',
	factor='295.0464')
