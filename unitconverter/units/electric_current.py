# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricCurrent(Unit):
    category = 'electric current'


# ampere is the SI unit of electric current
ampere = ElectricCurrent(
    name='ampere',
    factor='1',
    symbols='A',
    aliases=['amperes', 'amps', 'amp'],
    prefix_scaling='si')

# 1 abampere (biot) = 10 amps
abampere = ElectricCurrent(
    name='abampere',
    factor='10',
    symbols=['abA', 'Bi'],
    aliases=['abamperes', 'biot', 'biots'])

# 1 statampere = 3.335641E-10 amps
statampere = ElectricCurrent(
    name='statampere',
    factor='3.335641E-10',
    symbols='stA',
    aliases='statamperes')
