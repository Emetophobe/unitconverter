# Copyright (c) 2022-2023 Mike Cunningham

from enum import Enum
from unitconverter.unit import Unit


class Locale(Enum):
    """ English or American localization. """
    ENGLISH = 0
    AMERICAN = 1


def translate_unit(unit: Unit, locale: Locale) -> Unit:
    if locale == Locale.ENGLISH:
        return unit

    unit.name = _translate(unit.name)
    unit.aliases = [_translate(alias) for alias in unit.aliases]
    return unit


def _translate(name: str) -> str:
    for key, value in _translation_table.items():
        if key in name:
            name = name.replace(key, value)
    return name


_translation_table = {
    'metre': 'meter',
    'litre': 'liter',
}
