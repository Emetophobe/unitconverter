# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of pressure is the Pascal
pascal = Unit(
	name='pascal',
	symbols='Pa',
	aliases='pascals',
	factor='1')

bar = Unit(
	name='bar',
	aliases='bars',
	factor='1E+5')

barye = Unit(
	name='barye',
	symbols='Ba',
	aliases='baryes',
	factor='0.1')

psi = Unit(
	name='psi',
	symbols=['lbf/in^2', 'lbf/in2', 'lbs/in^2', 'lbs/in2'],
	aliases=['pounds per square inch', 'pound per square inch'],
	factor='6894.76')

torr = Unit(
	name='torr',
	symbols='Torr',
	aliases='torrs',
	factor='133.3224')

meter_of_mercury = Unit(
	name='meter of mercury',
	symbols=['mm Hg', 'mmHg'],
	aliases='meters of mercury',
	factor='133322.4')

inch_of_mercury = Unit(
	name='inch of mercury',
	symbols=['in Hg', 'inHg'],
	aliases='inches of mercury',
	factor='3386.389')

standard_atmosphere = Unit(
	name='standard atmosphere',
	symbols = ['atm'],
	aliases=['standard atmospheres'],
	factor='9.86923E-6')

technical_atmosphere = Unit(
	name='technical atmosphere',
	symbols = ['kgf/cm^2', 'kg/cm^2', 'kg/cm2'],
	aliases=['technical atmospheres', 'kilogram per square centimeter'],
	factor='1.01972E-5')
