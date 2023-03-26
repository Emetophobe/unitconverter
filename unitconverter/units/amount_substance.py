# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class AmountSubstance(Unit):
    category = 'amount of substance'


# The SI base unit for amount of substance is the mole.
mole = AmountSubstance(
    name='mole',
    factor='1',
    symbols='mol',
    aliases='moles',
    prefix_scaling='si')

# 1 atom is roughly 1.660538863127E-24 moles
atom = AmountSubstance(
    name='atom',
    factor='1.660538863127E-24',
    aliases='atoms',
    prefix_scaling='si')
