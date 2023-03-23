# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of force is the Newton
newton = Unit(
	name='newton',
	symbols='N',
	aliases='newtons',
	factor='1')

dyne = Unit(
	name='dyne',
	symbols='dyn',
	aliases='dynes',
	factor='1E-5')

poundal = Unit(
	name='poundal',
	symbols='pdl',
	aliases='poundals',
	factor='0.138254954376')

gram_force = Unit(
	name='gram-force',
	symbols=['gf', 'pond'],
	aliases='ponds',
	factor='9.80665E-3')

ounce_force = Unit(
	name='ounce-force',
	symbols='ozf',
	aliases='',
	factor='0.2780139')

pound_force = Unit(
	name='pound-force',
	symbols='lbf',
	aliases=['pounds of force', 'pound of force', 'lbs of force', 'lbs-force'],
	factor='4.448222')

tonne_force = Unit(
	name='tonne-force',
	symbols=['t-f', 'tf', 'MgF', 'mp'],
	aliases=['metric ton-force', 'megagram-force', 'megapond'],
	factor='9806.65')

long_ton_force = Unit(
	name='long ton-force',
	symbols='tnf',
	aliases='tf (long)',
	factor='9964.01641818352')

short_ton_force = Unit(
	name='short ton-force',
	symbols='tonf',
	aliases=['tf (short)'],
	factor='8896.443230521')

joule_per_meter = Unit(
	name='joule/meter',
	symbols=['J/m', 'j/m'],
	aliases='joules/meter',
	factor='1')
