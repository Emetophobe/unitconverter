# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations


class ElectricCharge(Unit):
    category = 'electric charge'


# coulomb is the SI unit of electric charge
coulomb = ElectricCharge(
    name='coulomb',
    factor='1',
    symbols='C',
    aliases='coulombs',
    prefix_scaling='si')

# 1 ampere second is equivalent to 1 coulomb
ampere_second = ElectricCharge(
    name='ampere second',
    factor='1',
    symbols=combinations(['A*', 'A-', 'A⋅'], ['sec', 's']),
    aliases=['ampere seconds', 'ampere-second', 'ampere-seconds'],
    prefix_scaling='si',
    prefix_index=0)

# 1 ampere minute = 60 coulomb
ampere_minute = ElectricCharge(
    name='ampere minute',
    factor='60',
    symbols=['A*min', 'A-min', 'A⋅min'],
    aliases=['ampere minutes', 'ampere-minute', 'ampere-minutes'],
    prefix_scaling='si',
    prefix_index=0)

# 1 ampere hour = 3600 coulomb
ampere_hour = ElectricCharge(
    name='ampere hour',
    factor='3600',
    symbols=combinations(['A*', 'A-', 'A⋅'], ['hr', 'h']),
    aliases=['ampere hours', 'ampere-hour', 'ampere-hours', 'amp-hours', 'amp-hour'],
    prefix_scaling='si',
    prefix_index=0)

# 1 franklin = roughly 3.335640951E-10 coulomb
franklin = ElectricCharge(
    name='franklin',
    factor='3.335640951E-10',
    symbols='fr',
    aliases=['franklins', 'statcoulomb'])
