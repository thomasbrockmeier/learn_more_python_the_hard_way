"""
cut
"""

import argparse
import sys


def cut(args):
    indices = [x.strip() for x in args.fields.split(',')]

    for line in sys.stdin:
        split_line = [x for x in line.split(args.delimiter) if x]

        try:
            for index in indices:
                if '-' in index:
                    x, y = index.split('-')
                    x, y = int(x), int(y)
                    print(' '.join(split_line[x:y]), end=' ')
                else:
                    print(split_line[int(index)], end=' ')
        except IndexError:
            pass
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python implementation of UNIX cut command"
    )

    parser.add_argument('delimiter', type=str, help='delimiter')
    parser.add_argument('fields', type=str, help='comma separated list of field indices, use "-" to indicate a range')

    cut(parser.parse_args())

