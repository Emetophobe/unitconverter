# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class Pressure(Unit):
    category = 'pressure'


# The pascal is the SI unit of pressure
pascal = Pressure(
    name='pascal',
    factor='1',
    symbols='Pa',
    aliases='pascals',
    prefix_scaling='si')

# 1 bar is exactly 100000 (1E+5) pascal
bar = Pressure(
    name='bar',
    factor='1E+5',
    aliases='bars',
    prefix_scaling='si')

# 1 barye is exactly 0.1 pascal
barye = Pressure(
    name='barye',
    factor='0.1',
    symbols='Ba',
    aliases='baryes',
    prefix_scaling='si')

# 1 metre of mercury is roughly 133322.4 pascal
metre_of_mercury = Pressure(
    name='metre of mercury',
    factor='133322.4',
    symbols=['m Hg', 'mHg'],
    aliases='metres of mercury',
    prefix_scaling='si',
    prefix_index=0)


# Non-SI units


# 1 psi is roughly 6894.757 pascal
psi = Pressure(
    name='pound per square inch',
    factor='6894.757',
    symbols=['psi', 'lbf/in^2', 'lbf/in2', 'lbs/in^2', 'lbs/in2'],
    aliases='pounds per square inch')

# 1 ksi = 1000 psi = 6.894757E+6 pascal
ksi = Pressure(
    name='kilopound per square inch',
    factor='6.894757E+6',
    symbols=['ksi', 'klbf/in^2', 'klbf/in2', 'klbs/in^2', 'klbs/in2'],
    aliases='kilopounds per square inch')

# 1 torr is roughly 133.322 pascal
torr = Pressure(
    name='torr',
    factor='133.322',
    symbols='Torr',
    aliases='torrs')

# 1 inch of mercury is roughly 3386.389 pascal
inch_of_mercury = Pressure(
    name='inch of mercury',
    factor='3386.389',
    symbols=['in Hg', 'inHg'],
    aliases='inches of mercury')

# 1 standard atmosphere = 101325 pascal
standard_atmosphere = Pressure(
    name='standard atmosphere',
    factor='101325',
    symbols='atm',
    aliases='standard atmospheres')

# 1 technical atmosphere = roughly 98066.5 pascal
technical_atmosphere = Pressure(
    name='technical atmosphere',
    factor='98066.5',
    symbols=['kgf/cm^2', 'kg/cm^2', 'kg/cm2'],
    aliases=['technical atmospheres', 'kilogram per square centimetre'])
