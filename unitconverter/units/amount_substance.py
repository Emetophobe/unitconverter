# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI base unit
mole = Unit(
    name='mole',
    symbols='mol',
    aliases='moles',
    factor='1')

atom = Unit(
	name='atom',
	symbols='',
	aliases='atoms',
	factor='1.660538863127E-24')
