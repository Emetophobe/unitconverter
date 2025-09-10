# Unit Converter

A basic unit converter written in Python.

This script is meant to be used as a command line utility. If you're looking for a
python library I recommend [pint][1] or [astropy][2].

## Features

Units can be prefixed based on a prefix scaling option. The default prefix
scaling behaviour can be changed on a per-unit basis.

The following prefix options are currently supported:

    none        - don't use prefix scaling (default)
    metric      - use metric prefix table (quecto to quetta)
    binary      - use binary prefix table (kibi to yobi and kilo to yotta)

Units can be combined to create composite units. You can create a composite unit
from any of the defined units (excluding temperature units). Temperature units use
a custom conversion function and don't work well with other units for now.

For example you can create a speed unit by dividing any `length` unit by any `time` unit:

    $ python convert.py 1 metre/second inches/day -p 2
    1 metre/second = 3401574.8 inches/day

Unit composition is an experimental feature and there are still bugs to be sorted out.


## Requirements

    Python 3.12 or newer

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: convert.py [-h] [-f | -e | -s] [-p ndigits] [-n] quantity source target [target ...]

    positional arguments:
      quantity              quantity or value (an integer, float, or fraction)
      source                the source unit
      target                one or more target units

    options:
      -h, --help            show this help message and exit
      -f, --fraction        display results using fractions
      -e, --exponent        display results using scientific e notation
      -s, --separators      display results using thousands separators
      -p, --precision ndigits
                            set rounding precision (default: None)
      -n, --normalize       normalize result by stripping trailing zeros

## Examples

#### Basic usage

    $ python convert.py 1024 bytes kibibytes
    1024 bytes = 1 kibibytes

    $ python convert.py 600 seconds minutes
    600 seconds = 10 minutes

#### Unit names can be symbols, plural forms, or other aliases

    $ python convert.py 10 cm metres
    10 cm = 0.1 metres

    $ python convert.py 10 amps kA
    10 amps = 0.01 kA

#### Convert multiple units at once by specifying multiple target units

    $ python convert.py 1 mile furlongs yards feet inches
    1 mile = 8 furlongs
           = 1760 yards
           = 5280 feet
           = 63360 inches

#### Set rounding precision with `-p` or `--precision`

    $ python convert.py 10 metres inches -p 3
    10 metres = 393.701 inches

#### Display results using fractions with `-f` or `--fraction`

    $ python convert.py 3 inch foot -f
    3 inch = 1/4 foot

#### Display results using scientific e notation with `-e` or `--exponent`

    $ python convert.py 5 cm nm -e
    5 cm = 5E+7 nm

#### Display results using thousands separators with `-s` or `--separators`

    $ python convert.py 5 cm nm --separators
    5 cm = 50,000,000 nm

#### Units can be converted as long as they have the same dimension (length, time, mass, etc..)

    $ python convert.py 1 metre hectare
    Error: Can't convert between metre and hectare

    $ python convert.py 1 metre² hectare
    1 metre² = 0.0001 hectare

#### Unit composition is possible with any of the pre-defined units. Multiplication, division, and exponents are currently supported.

    $ python convert.py 1 watt amp*volt joule/second
    1 watt = 1 amp*volt
           = 1 joule/second

    $ python convert.py 1 joule kg*m²/s² watt*second coulomb*volt
    1 joule = 1 kg*m²/s²
            = 1 watt*second
            = 1 coulomb*volt

#### Multi-word unit names are also supported but they need to be wrapped in quotes, otherwise the parser will think they're separate units

    $ python convert.py 1 "astronomical unit" metres
    1 astronomical unit = 149597870700 metres

#
### Note: This script is a work in progress. Bug reports and suggestions are welcome.


[1]: https://github.com/hgrecco/pint/
[2]: https://github.com/astropy/astropy
