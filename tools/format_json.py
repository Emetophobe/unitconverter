#!/usr/bin/env python
# Copyright (c) 2022-2023 Mike Cunningham

import json
import hashlib
from pathlib import Path


def file_checksum(filename, algorithm='sha256'):
    """ Returns a file checksum. """
    with open(filename, 'rb') as infile:
        # file_digest() requires Python 3.11, but my converter targets 3.9
        # TODO: write a custom file_digest?
        return hashlib.file_digest(infile, algorithm).hexdigest()


def format_files(paths: list[str], indent: int = 2, sort_keys: bool = False):
    """ Format json files in the specified path(s).

    Args:
        paths (list[str]): list of json files or directories.
        indent (int, optional): json indent level. Defaults to 2.
        sort_keys (bool, optional): sort json keys. Defaults to False.
    """

    # Get unique json files from paths
    uniques = set()
    for path in paths:
        path = Path(path)
        if path.is_file() and path.name.endswith('.json'):
            uniques.add(path.resolve())
        elif path.is_dir():
            for path in path.rglob('*.json'):
                uniques.add(path.resolve())
        else:
            raise FileNotFoundError(path)

    # Format all selected json files
    for path in uniques:
        # Load json
        old_checksum = file_checksum(path)
        with open(path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)

        # Save formatted json
        with open(path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=indent, sort_keys=sort_keys)
            outfile.write('\n')  # add trailing newline

        # Check if file format changed
        new_checksum = file_checksum(path)
        if old_checksum != new_checksum:
            print('Updated', path)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'paths',
        help='file or directory paths',
        nargs='+')

    parser.add_argument(
        '-i', '--indent',
        help='specify an indent level (default: %(default)s)',
        default=2,
        type=int)

    parser.add_argument(
        '-s', '--sortkeys',
        help='sort dictionary keys (default: %(default)s)',
        action='store_true',
        dest='sort_keys')

    args = parser.parse_args()

    try:
        format_files(**vars(args))
    except OSError as e:
        print('Error:', e)
