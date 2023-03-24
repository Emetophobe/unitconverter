# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The lumen is the SI unit of luminous flux
lumen = Unit(
	name='lumen',
	symbols='lm',
	aliases='lumens',
	factor='1')

# 1 candela steradian is equal to 1 lumen
candela_steradian = Unit(
	name='candela-steradian',
	symbols=['cd·sr', 'cd*sr', 'cd-sr'],
	aliases='candela steradian',
	prefix_index=0,
	factor='1')
