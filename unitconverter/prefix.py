# Copyright (c) 2022-2023 Mike Cunningham


# A unit supports one of the following prefix options:
PREFIX_OPTIONS = [
    'none',     # don't generate any prefixes
    'binary',   # generate binary prefixes
    'decimal',  # generate decimal prefixes
    'both',     # generate decimal prefixes and binary prefixes
    'all',      # generate SI prefixes and binary prefixes
    'si'        # generate SI prefixes [default]
]


# SI prefixes
SI_PREFIXES = [
    ('1E-30', 'q', 'quecto'),
    ('1E-27', 'r', 'ronto'),
    ('1E-24', 'y', 'yocto'),
    ('1E-21', 'z', 'zepto'),
    ('1E-18', 'a', 'atto'),
    ('1E-15', 'f', 'femto'),
    ('1E-12', 'p', 'pico'),
    ('1E-9', 'n', 'nano'),
    ('1E-6', 'µ', 'micro'),
    ('1E-3', 'm', 'milli'),
    ('1E-2', 'c', 'centi'),
    ('1E-1', 'd', 'deci'),
    ('1E+1', 'da', 'deca'),
    ('1E+2', 'h', 'hecto'),
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]

# Decimal prefixes (kilo to quetta)
DECIMAL_PREFIXES = [
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]

# binary prefixes
BINARY_PREFIXES = [
    ('2E+10', 'Ki', 'kibi'),
    ('2E+20', 'Mi', 'mebi'),
    ('2E+30', 'Gi', 'gibi'),
    ('2E+40', 'Ti', 'tebi'),
    ('2E+50', 'Pi', 'pebi'),
    ('2E+60', 'Ei', 'exbi'),
    ('2E+70', 'Zi', 'zebi'),
    ('2E+80', 'Yi', 'yobi'),
]


def get_prefix_table(prefix_option: str) -> list[tuple[str, str, str]]:
    if not prefix_option:
        return []
    elif prefix_option == 'all':
        return SI_PREFIXES + BINARY_PREFIXES
    elif prefix_option == 'both':
        return DECIMAL_PREFIXES + BINARY_PREFIXES
    elif prefix_option == 'binary':
        return BINARY_PREFIXES
    elif prefix_option == 'decimal':
        return DECIMAL_PREFIXES
    elif prefix_option == 'si':
        return SI_PREFIXES
    else:
        raise ValueError(f'Unsupported prefix option: {prefix_option}')
