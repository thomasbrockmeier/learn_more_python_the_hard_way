"""
grep
"""

import argparse
import re


def grep(args):
    for filename in args.filenames:
        with open(filename, 'r') as fh:
            for line in fh.readlines():
                formatted = ''
                start = end = old_start = old_end = None

                matches = re.finditer(args.pattern, line)
                for match in matches:
                    if start:
                        old_start, old_end = start, end

                    start, end = match.span()

                    if old_start:
                        formatted += line[old_end:start]
                    else:
                        formatted += line[:start]

                    formatted += '\033[91m'
                    formatted += line[start:end]
                    formatted += '\033[0m'

                if end:
                    formatted += line[end:]

                if formatted:
                    print(formatted, end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python implementation of UNIX grep command"
    )

    parser.add_argument('pattern', type=str, help='pattern')
    parser.add_argument('filenames', type=str, nargs='+', help='filenames')
    grep(parser.parse_args())
