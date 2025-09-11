#!/usr/bin/env python
# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import sys
import argparse
import logging
import traceback

from unitconverter.converter import UnitConverter
from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_quantity


def print_error(msg: str, status: int = 1) -> None:
    """ Print an error message and exit. """
    print(msg, file=sys.stderr)
    sys.exit(status)


def print_traceback(error: Exception) -> None:
    """ Print a stack trace and exit. """
    traceback.print_exception(error, chain=False)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "quantity",
        help="quantity or value (an integer, float, or fraction)")

    parser.add_argument(
        "source",
        help="the source unit")

    parser.add_argument(
        "target",
        help="one or more target units",
        nargs="+")

    subgroup = parser.add_mutually_exclusive_group()

    subgroup.add_argument(
        "-f", "--fraction",
        help="display results using fractions",
        action="store_true")

    subgroup.add_argument(
        "-e", "--exponent",
        help="display results using scientific e notation",
        action="store_true")

    subgroup.add_argument(
        "-s", "--separators",
        help="display results using thousands separators",
        action="store_true")

    parser.add_argument(
        "-p", "--precision",
        help="set rounding precision (default: %(default)s)",
        metavar="ndigits",
        default=None,
        type=int)

    parser.add_argument(
        "-n", "--normalize",
        help="normalize result by stripping trailing zeros",
        action="store_true")

    parser.add_argument(
        "--debug",
        help=argparse.SUPPRESS,
        action="store_true")

    args = parser.parse_args()

    # Check precision
    if args.precision is not None and (args.precision < 0 or args.precision > 30):
        print_error("Error: Precision must be between 0 and 30")

    # Configure debug logger
    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.WARNING)
    logging.basicConfig(format="debug: %(message)s")

    results = []

    # Perform conversions
    try:
        converter = UnitConverter()
        for target in args.target:
            results.append((converter.convert(args.quantity, args.source, target), target))
    except (ConverterError, TypeError, ValueError) as error:
        print_traceback(error) if args.debug else print_error(f"Error: {error}")

    # Display results
    padding = " " * len(f"{args.quantity} {args.source}")
    for index, (result, target) in enumerate(results):
        result = format_quantity(result,
                                 args.precision,
                                 args.normalize,
                                 args.fraction,
                                 args.exponent,
                                 args.separators)
        if index == 0:
            print(f"{args.quantity} {args.source} = {result} {target}")
        else:
            print(f"{padding} = {result} {target}")


if __name__ == "__main__":
    main()
