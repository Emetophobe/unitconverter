# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The katal is the SI unit of catalytic activity.
katal = Unit(
    name='katal',
    factor='1',
    symbols='kat',
    aliases='katals',
    prefix_scaling='si')

# 1 mole/sec is equal to 1 katal
mole_per_second = Unit(
    name='mole per second',
    factor='1',
    symbols='mol/s',
    aliases=['moles per second', 'moles/second', 'mole/second', 'moles/sec',
             'mole/sec', 'moles/s', 'mole/s'],
    prefix_scaling='si',
    prefix_index=0)
