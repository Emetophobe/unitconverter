# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit for electric current
ampere = Unit(
    name='ampere',
    symbols='A',
    aliases=['amperes', 'amps', 'amp'],
    factor='1',
    category='electric current',
    prefix_scaling='si')

# Electric charge
coulomb = Unit(
    name='coulomb',
    symbols='C',
    aliases='coulombs',
    factor='1',
    category='electric charge',
    prefix_scaling='si')

# Electric potential
volt = Unit(
    name='volt',
    symbols='V',
    aliases='volts',
    factor='1',
    category='electric potential',
    prefix_scaling='si')

# Electrical capacitance
farad = Unit(
    name='farad',
    symbols='F',
    aliases='farads',
    factor='1',
    category='electrical capacitance',
    prefix_scaling='si')

# Electrical conductance
siemens = Unit(
    name='siemens',
    symbols='S',
    factor='1',
    category='electrical conductance',
    prefix_scaling='si')

# Electrical inductance
henry = Unit(
    name='henry',
    symbols='H',
    aliases='henries',
    factor='1',
    category='electrical inductance',
    prefix_scaling='si')

# Electrical resistance
ohm = Unit(
    name='ohm',
    symbols='Ω',
    aliases='ohms',
    factor='1',
    category='electrical resistance',
    prefix_scaling='si')
