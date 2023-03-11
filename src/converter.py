# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal
from src.units import all_unit_values


class Converter:
    def __init__(self, units):
        self.units = units

    def convert(self, value, source, dest):
        """ Convert a number from source unit to dest unit.

        Args:
            value (Decimal): the decimal number to convert.
            source (str): the source unit name.
            dest (str): the destination unit name.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            KeyError: if the source or dest unit is invalid.
        """
        value = Decimal(value)

        if source == dest or value == 0:
            return value

        source_unit = self.units[source]
        dest_unit = self.units[dest]

        source_value = Decimal(source_unit)
        dest_value = Decimal(dest_unit)

        return value * (source_value / dest_value)


class Temperature:
    """ Temperature conversion requires a specialized converter. """

    def convert(self, value, source, dest):
        """ Convert between temperatures using kelvin as a baseline.

        Args:
            value (Decimal): the decimal value to convert.
            source (str): the source unit name.
            dest (str): the destination unit name.

        Returns:
            Decimal: the result of the conversion.

        Raises:
            KeyError: if the source or dest unit is invalid.
        """
        kelvin = self.to_kelvin(value, source)
        return self.from_kelvin(kelvin, dest)

    def to_kelvin(self, value, source_unit):
        if source_unit == 'celcius':
            return value + Decimal(273.15)
        elif source_unit == 'fahrenheit':
            return (value + Decimal(459.67)) * Decimal(5 / 9)
        elif source_unit == 'rankine':
            return value * Decimal(5 / 9)
        elif source_unit == 'kelvin':
            return value
        else:
            raise KeyError(source_unit)

    def from_kelvin(self, value, dest_unit):
        if dest_unit == 'celcius':
            return value - Decimal(273.15)
        elif dest_unit == 'fahrenheit':
            return value * Decimal(9 / 5) - Decimal(459.67)
        elif dest_unit == 'rankine':
            return value * Decimal(9 / 5)
        elif dest_unit == 'kelvin':
            return value
        else:
            raise KeyError(dest_unit)


def get_converter(name):
    """ Get a converter instance based on the category.

    Args:
        name (str): the converter category (i.e "length").

    Raises:
        ValueError: if the category name is invalid.

    Returns:
        Converter: an instance of the Converter (or Temperature) class.
    """
    if name == 'temperature':
        return Temperature()

    elif name in all_unit_values.keys():
        return Converter(all_unit_values[name])

    raise ValueError(f'Invalid category: {name}')
