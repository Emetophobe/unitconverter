# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The pascal is the SI unit of pressure
pascal = Unit(
    name='pascal',
    symbols='Pa',
    aliases='pascals',
    factor='1')

# 1 bar is exactly 100000 (1E+5) pascal
bar = Unit(
    name='bar',
    aliases='bars',
    factor='1E+5')

# 1 barye is exactly 0.1 pascal
barye = Unit(
    name='barye',
    symbols='Ba',
    aliases='baryes',
    factor='0.1')

# 1 psi is roughly 6894.757 pascal
psi = Unit(
    name='psi',
    symbols=['lbf/in^2', 'lbf/in2', 'lbs/in^2', 'lbs/in2'],
    aliases=['pounds per square inch', 'pound per square inch'],
    prefix_index=0,
    factor='6894.757')

# 1 torr is roughly 133.322 pascal
torr = Unit(
    name='torr',
    symbols='Torr',
    aliases='torrs',
    factor='133.322')

# 1 meter of mercury is roughly 133322.4 pascal
meter_of_mercury = Unit(
    name='meter of mercury',
    symbols=['m Hg', 'mHg'],
    aliases='meters of mercury',
    prefix_index=0,
    factor='133322.4')

# 1 inch of mercury is roughly 3386.389 pascal
inch_of_mercury = Unit(
    name='inch of mercury',
    symbols=['in Hg', 'inHg'],
    aliases='inches of mercury',
    prefix_index=0,
    factor='3386.389')

# 1 standard atmosphere = 101325 pascal
standard_atmosphere = Unit(
    name='standard atmosphere',
    symbols = ['atm'],
    aliases=['standard atmospheres'],
    prefix_scaling='none',
    factor='101325')

# 1 technical atmosphere = roughly 98066.5 pascal
technical_atmosphere = Unit(
    name='technical atmosphere',
    symbols = ['kgf/cm^2', 'kg/cm^2', 'kg/cm2'],
    aliases=['technical atmospheres', 'kilogram per square centimeter'],
    prefix_scaling='none',
    factor='98066.5')
