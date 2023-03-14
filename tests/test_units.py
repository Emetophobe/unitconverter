# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase, Unit


class TestUnits(AbstractTestCase):

    def test_duplicates(self) -> None:
        """ Search for duplicate names, symbols or aliases. """
        msg = 'Duplicate name or alias: {}'
        aliases = {}

        for unit in self.get_units():
            self.assertNotIn(unit.name, aliases.keys(), msg.format(unit.name))
            aliases[unit.name] = unit

            for alias in unit.aliases:
                self.assertNotIn(alias, aliases.keys(), msg.format(alias))
                aliases[alias] = unit

    def get_units(self) -> Unit:
        """ Iterate over the unit categories and yield Units. """
        for category, units in self.all_units.items():
            for unitname, properties in units.items():
                yield Unit(unitname, category, **properties)
