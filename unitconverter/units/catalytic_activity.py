# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The katal is the SI unit of catalytic activity.
katal = Unit(
    name='katal',
    symbols='kat',
    aliases='katals',
    factor='1')

# 1 mole/sec is equal to 1 katal
mole_per_second = Unit(
    name='mole per second',
    symbols='mol/s',
    aliases=['moles per second', 'moles/s', 'mole/s'],
    prefix_index=0,	 # prefix first word
    factor='1')
