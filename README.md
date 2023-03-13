# A basic unit converter written in Python 3

The following unit categories are currently supported:

* Area
* Bytes
* Length
* Mass
* Temperature
* Time
* Volume


## Requirements:

    Python 3.9 or newer.

## Installation:

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage:

    usage: converter.py [-h] [-p size] [-c] [-l] value source dest

    A simple unit converter.

    positional arguments:
    value                 integer or float value to convert.
    source                name of the source unit.
    dest                  name of the destination unit.

    options:
    -h, --help            show this help message and exit
    -p size, --precision size
                            rounding precision (default: None)
    -c, --comma           show thousands separator (default: False)
    -l, --list            list unit categories and exit


## Examples:

    $ ./converter.py 1024 bytes kibibytes
    1024 bytes = 1 kibibytes

    $ ./converter.py 600 seconds minutes
    600 seconds = 10 minutes

Unit names can be a shortform or symbol:

    $ ./converter.py 10 centimeters meters
    10 centimeters = 0.1 meters

    $ ./converter.py 10 centimeter m
    10 centimeter = 0.1 m

    $ ./converter.py 10 cm m
    10 cm = 0.1 m

Set decimal precision with `--precision`/`-p`:

    $ ./converter.py 12 meters inches -p 5
    12 meters = 472.44094 inches

Display thousands separators with `--comma`/`-c`:

    $ ./converter.py 5 cm nm -c
    5 cm = 50,000,000 nm

Multi word unit names are also supported, but for now they need to be wrapped in quotes; i.e "cubic meters":

    $ ./converter.py 1 "cubic meters" liters
    1 cubic meters = 1000 liters

    $ ./converter.py 1 "cu m" liters
    1 cu m = 1 liters

Many multi-word units also have a shortform, i.e "cubic meters" can also be represented as "m3" or "m^3":

    $ ./converter.py 1 m3 liter
    1 m3 = 1000 liter

    $ ./converter.py 1 m^3 liter
    1 m^3 = 1000 liter
