"""
cat
"""

import argparse


def cat(filenames, number):
    for filename in filenames:
        print(f'Filename: {filename}')
        with open(filename, 'r') as f:
            num = 1
            for line in f:
                print(f'{num if number else ""} {line}', end='')
                num += 1
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python implementation of UNIX cat command"
    )

    parser.add_argument('filenames', type=str, nargs='+', help='filenames')
    parser.add_argument('-n', '--number', action='store_true', help='filenames')
    args = parser.parse_args()
    cat(args.filenames, args.number)

