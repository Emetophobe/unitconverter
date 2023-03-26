# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricalCapacitance(Unit):
    category = 'electrical capacitance'


# farad is the SI unit of electrical capacitance
farad = ElectricalCapacitance(
    name='farad',
    factor='1',
    symbols='F',
    aliases='farads',
    prefix_scaling='si')

# 1 coulomb/volt is equivalent to 1 farad
coulomb_per_volt = ElectricalCapacitance(
    name='coulomb per volt',
    factor='1',
    symbols='C/V',
    aliases=['coulombs per volt', 'coulomb/volt', 'coulombs/volt'],
    prefix_scaling='si',
    prefix_index=0)

# 1 abfarad = 1E+9 farads
abfarad = ElectricalCapacitance(
    name='abfarad',
    factor='1E+9',
    symbols='abF',
    aliases='abfarads')

# 1 statfarad = 1.112650056E-12 farads
statfarad = ElectricalCapacitance(
    name='statfarad',
    factor='1.112650056E-12',
    symbols='stF',
    aliases='statfarads')
