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
