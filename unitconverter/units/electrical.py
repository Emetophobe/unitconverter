# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricCurrent(Unit):
    category = 'electric current'


class ElectricCharge(Unit):
    category = 'electric charge'


class ElectricPotential(Unit):
    category = 'electric potential'


class ElectricalCapacitance(Unit):
    category = 'electrical capacitance'


class ElectricalConductance(Unit):
    category = 'electrical conductance'


class ElectricalInductance(Unit):
    category = 'electrical inductance'


class ElectricalResistance(Unit):
    category = 'electrical resistance'


# ampere is the SI unit of electric current
ampere = ElectricCurrent(
    name='ampere',
    factor='1',
    symbols='A',
    aliases=['amperes', 'amps', 'amp'],
    prefix_scaling='si')

# coulomb is the SI unit of electric charge
coulomb = ElectricCharge(
    name='coulomb',
    factor='1',
    symbols='C',
    aliases='coulombs',
    prefix_scaling='si')

# volt is the SI unit of electric potential
volt = ElectricPotential(
    name='volt',
    factor='1',
    symbols='V',
    aliases='volts',
    prefix_scaling='si')

# farad is the SI unit of electrical capacitance
farad = ElectricalCapacitance(
    name='farad',
    factor='1',
    symbols='F',
    aliases='farads',
    prefix_scaling='si')

# siemens is the SI unit of electrical conductance
siemens = ElectricalConductance(
    name='siemens',
    factor='1',
    symbols='S',
    prefix_scaling='si')

# henry is the SI unit of electrical inductance
henry = ElectricalInductance(
    name='henry',
    factor='1',
    symbols='H',
    aliases='henries',
    prefix_scaling='si')

# ohm is the SI unit of electrical resistance
ohm = ElectricalResistance(
    name='ohm',
    factor='1',
    symbols='Ω',
    aliases='ohms',
    prefix_scaling='si')
