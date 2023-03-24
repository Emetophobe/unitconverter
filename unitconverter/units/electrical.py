# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit for electric current
ampere = Unit(
    name='ampere',
    symbols='A',
    aliases=['amperes', 'amps', 'amp'],
    factor='1',
    category='electric current')

# Electric charge
coulomb = Unit(
    name='coulomb',
    symbols='C',
    aliases='coulombs',
    factor='1',
    category='electric charge')

# Electric potential
volt = Unit(
    name='volt',
    symbols='V',
    aliases='volts',
    factor='1',
    category='electric potential')

# Electrical capacitance
farad = Unit(
    name='farad',
    symbols='F',
    aliases='farads',
    factor='1',
    category='electrical capacitance')

# Electrical conductance
siemens = Unit(
    name='siemens',
    symbols='S',
    factor='1',
    category='electrical conductance')

# Electrical inductance
henry = Unit(
    name='henry',
    symbols='H',
    aliases='henries',
    factor='1',
    category='electrical inductance')

# Electrical resistance
ohm = Unit(
    name='ohm',
    symbols='Ω',
    aliases='ohms',
    factor='1',
    category='electrical resistance')
