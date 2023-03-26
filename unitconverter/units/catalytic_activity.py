# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_SECOND


class CatalyticActivity(Unit):
    category = 'catalytic activity'


# The katal is the SI unit of catalytic activity
katal = CatalyticActivity(
    name='katal',
    factor='1',
    symbols='kat',
    aliases='katals',
    prefix_scaling='si')

# 1 mole/sec is equal to 1 katal
mole_per_second = CatalyticActivity(
    name='mole per second',
    factor='1',
    symbols='mol/s',
    aliases=combinations(['mole', 'moles'], PER_SECOND),
    prefix_scaling='si',
    prefix_index=0)
