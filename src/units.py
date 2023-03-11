# Copyright (c) 2022-2023 Mike Cunningham


area_values = {
    'acres': '4046.8564224',
    'ares': '100.0',
    'circular inches': '0.000506707479',
    'hectares': '10000.0',
    'hides': '485000.0',
    'roods': '1011.7141056',
    'square centimeters': '0.0001',
    'square feet': '0.09290304',
    'square feet (US)': '0.092903411613',
    'square inches': '0.00064516',
    'square kilometers': '1000000.0',
    'square meters': '1.0',
    'square micrometers': '1e-12',
    'square miles': '2589988.110336',
    'square millimeters': '1e-06',
    'square nanometers': '1e-18',
    'square rods (poles)': '25.29285264',
    'square yards': '0.83612736',
    'squares': '9.290304',
    'townships': '93239571.972'
}

area_names = {
    'acres': ['acre', 'ac'],
    'ares': ['are', 'a'],
    'circular inches': ['circular inch', 'c in'],
    'hectares': ['hectare', 'ha'],
    'hides': ['hide'],
    'roods': ['rood'],
    'square centimeters': ['square centimeter', 'sq cm'],
    'square feet': ['square foot', 'sq ft'],
    'square feet (US)': ['square foot (US)', 'sq ft (US)'],
    'square inches': ['square inch', 'sq in'],
    'square kilometers': ['square kilometer', 'sq km'],
    'square meters': ['square meter', 'sq m'],
    'square micrometers': ['square micrometer'],
    'square miles': ['square mile', 'sq mi'],
    'square millimeters': ['square millimeter', 'sq mm'],
    'square nanometers': ['square nanometer', 'sq nm'],
    'square rods (poles)': ['square rod', 'sq rod'],
    'square yards': ['square yard', 'sq yd'],
    'squares': ['square'],
    'townships': ['township']
}

length_values = {
    'centimeters': '0.01',
    'decimeters': '0.1',
    'feet': '0.3048',
    'inches': '0.0254',
    'kilometers': '1000.0',
    'meters': '1.0',
    'micrometers': '1e-06',
    'miles': '1609.344',
    'millimeters': '0.001',
    'nanometers': '1e-09',
    'yards': '0.9144'
}

length_names = {
    'centimeters': ['centimeter', 'cm'],
    'decimeters': ['decimeter', 'dm'],
    'feet': ['foot', 'ft'],
    'inches': ['inch', 'in'],
    'kilometers': ['kilometer', 'km'],
    'meters': ['meter', 'm'],
    'micrometers': ['micrometer'],
    'miles': ['mile', 'mi'],
    'millimeters': ['millimeter', 'mm'],
    'nanometers': ['nanometer', 'nm'],
    'yards': ['yard', 'y']
}

bytes_values = {
    'bits': '0.125',
    'bytes': '1.0',
    'gigabits': '134217728.0',
    'gigabytes': '1073741824.0',
    'kilobits': '128.0',
    'kilobytes': '1024.0',
    'megabits': '131072.0',
    'megabytes': '1048576.0',
    'petabits': '140737488355328.0',
    'petabytes': '1125899906842624.0',
    'terabits': '137438953472.0',
    'terabytes': '1099511627776.0'
}

bytes_names = {
    'bits': ['bit', 'b'],
    'bytes': ['byte', 'B'],
    'gigabits': ['gigabit', 'Gb'],
    'gigabytes': ['gigabyte', 'GB'],
    'kilobits': ['kilobit', 'Kb'],
    'kilobytes': ['kilobyte', 'KB'],
    'megabits': ['megabit', 'Mb'],
    'megabytes': ['megabyte', 'MB'],
    'petabits': ['petabit', 'Pb'],
    'petabytes': ['petabyte', 'PB'],
    'terabits': ['terabit', 'Tb'],
    'terabytes': ['terabyte', 'TB']
}

temperature_names = {
    'celcius': ['c'],
    'fahrenheit': ['f'],
    'kelvin': ['k'],
    'rankine': ['r']
}

all_unit_values = {
    'area': area_values,
    'bytes': bytes_values,
    'length': length_values,
    'temperature': None,  # Temperature is a special case
}

all_unit_names = {
    'area': area_names,
    'bytes': bytes_names,
    'length': length_names,
    'temperature': temperature_names,
}


def find_unit(name):
    """ Find a unit matching the specified name or alias.

    Returns:
        tuple[str, str]: the unit category and name.

    Raises:
        ValueError: if name was not found.
    """
    for category, units in all_unit_names.items():
        for unitname, aliases in units.items():
            if name == unitname or name in aliases:
                return (category, unitname)

    raise ValueError(f'Unsupported unit name: {name}')
