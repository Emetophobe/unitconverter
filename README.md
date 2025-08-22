# Unit Converter

A basic unit converter written in Python.

This script is meant to be used as a command line utility. If you're looking for a
python library there are superior alternatives such as [pint][1] or [astropy][2].

## Features

Units are prefixed based on a prefix scaling option. The default prefix
scaling behaviour can be changed on a per-unit basis.

The following prefix options are currently supported:

    none        - don't use prefix scaling (default)
    metric      - use metric prefix table (quecto to quetta)
    binary      - use binary prefix table (kibi to yobi)


Units can be combined to create composite units. You can create a composite unit
from any of the defined units (excluding temperature units). Temperature units use
a custom conversion function and don't work well with other units for now.

For example you can create a speed unit by dividing any `length` unit by any `time` unit:

    $ python convert.py 1 metre/second inches/day -p 2
    1 metre/second = 3401574.8 inches/day

Many other unit combinations are possible:

    $ python convert.py 1 watt amp*volt joule/second
    1 watt = 1 amp*volt
           = 1 joule/second

    $ python convert.py 1 joule kg*m2*s^-2 watt*second coulomb*volt
    1 joule = 1 kg*m2*s^-2
            = 1 watt*second
            = 1 coulomb*volt

Unit composition is an experimental feature and there are still bugs to be sorted out.


## Requirements

    Python 3.11 or newer

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: convert.py [-h] [-p ndigits] [-n] [-s] [-e] value source dest [dest ...]

    positional arguments:
    value                       decimal or integer value
    source                      source unit
    dest                        one or more destination units

    options:
    -h, --help                  show this help message and exit
    -p, --precision ndigits     set rounding precision (default: None)
    -n, --normalize             normalize result by stripping rightmost trailing zeros
    -s, --separators            show thousands separator (default: False)
    -e, --exponent              show E notation when possible (default: False)


## Examples

#### Basic usage

    $ python convert.py 1024 bytes kibibytes
    1024 bytes = 1 kibibytes

    $ python convert.py 600 seconds minutes
    600 seconds = 10 minutes

#### Unit names can be symbols, plural forms, or other aliases

    $ python convert.py 10 cm m
    10 cm = 0.1 m

    $ python convert.py 10 amps kA
    10 amps = 0.01 kA

#### Convert multiple units at once

    $ python convert.py 1 metre cm in ft -p 4
    1 metre = 100.0000 cm
            = 39.3701 in
            = 3.2808 ft

#### Use mathematical expressions to create composite units (experimental)

    $ python convert.py 1 watt volt*amp joule/sec
    1 watt = 1 volt*amp
           = 1 joule/sec


#### Set rounding precision with `-p`/`--precision`

    $ python convert.py 12 metres inches -p 5
    12 metres = 472.44094 inches

#### Display thousands separators with `-s`/`--separators`

    $ python convert.py 5 cm nm -c
    5 cm = 50,000,000 nm

#### Show E notation with `-e`/`--exponent`

    $ python convert.py 5 cm nm -e
    5 cm = 5E+7 nm


#### Multi-word unit names are also supported but they need to be wrapped in quotes

    $ python convert.py 1 "US survey acre" km^2 -p 8
    1 US survey acre = 0.00404687 km^2

#
### Note: This script is a work in progress. Bug reports and suggestions are welcome.


[1]: https://github.com/hgrecco/pint/
[2]: https://github.com/astropy/astropy
