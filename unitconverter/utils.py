# Copyright (c) 2022-2023 Mike Cunningham


def combinations(prefixes, suffixes, excludes=None):
    """ Create prefix + suffix combinations from two string lists. """
    if not isinstance(prefixes, (list, tuple)):
        raise TypeError(f'{prefixes!r} is not a list or tuple.')

    if not isinstance(suffixes, (list, tuple)):
        raise TypeError(f'{suffixes!r} is not a list or tuple.')

    excludes = excludes or []
    names = []
    for prefix in prefixes:
        for suffix in suffixes:
            merged = prefix + suffix
            if merged not in names and merged not in excludes:
                names.append(merged)

    return names


# Tuples of commonly used prefixes and suffixes
METRE_NAMES = ('metre', 'metres', 'meter', 'meters')
LITRE_NAMES = ('litre', 'litres', 'liter', 'litres')
AMPERE_NAMES = ('ampere', 'amperes', 'amp', 'amps')

# Leading space before 'per' is intentional
PER_SECOND = (' per second', '/second', '/sec', '/s')
PER_MINUTE = (' per minute', '/minute', '/min')
PER_HOUR = (' per hour', '/hour', '/hr')
PER_METRE = combinations([' per ', '/'], ['metre', 'meter'])
PER_LITRE = combinations([' per ', '/'], ['litre', 'liter'])
PER_AMPERE = [' per ampere', ' per amp', '/ampere', '/amp']
