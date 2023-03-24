# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The SI base unit for amount of substance is the mole.
mole = Unit(
    name='mole',
    symbols='mol',
    aliases='moles',
    factor='1')

# 1 atom is roughly 1.660538863127E-24 moles
atom = Unit(
    name='atom',
    aliases='atoms',
    factor='1.660538863127E-24')
