#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import json
import hashlib
from pathlib import Path


def file_checksum(filename, algorithm='sha256'):
    with open(filename, 'rb') as infile:
        return hashlib.file_digest(infile, algorithm).hexdigest()


def format_json(filename, indent=2, sort_keys=False):
    """ Format a json file. """
    old_checksum = file_checksum(filename)

    with open(filename, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=indent, sort_keys=sort_keys)
        outfile.write('\n')  # add trailing newline

    new_checksum = file_checksum(filename)
    if old_checksum != new_checksum:
        print('Updated', filename)


def format_files(indent=2, sort_keys=False):
    """ Format all json files. """
    for path in Path('./data/').glob('*.json'):
        format_json(path, indent, sort_keys)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--filename',
        help='specify a json file',
        type=Path)

    parser.add_argument(
        '-i', '--indent',
        help='specify an indent level (default: %(default)s)',
        default=2,
        type=int
    )

    parser.add_argument(
        '-s', '--sortkeys',
        help='sort dictionary keys (default: %(default)s)',
        action='store_true'
    )

    args = parser.parse_args()

    try:
        if args.filename:
            format_json(args.filename, args.indent, args.sortkeys)
        else:
            format_files(args.indent, args.sortkeys)
    except OSError as e:
        print('Error:', e)
