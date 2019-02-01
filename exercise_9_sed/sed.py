"""
sed
"""

import argparse
import re
import sys


def sed(args):
    regex = re.compile('s/(?P<query>[\w\W]+)/(?P<replacement>[\w\d\s]*)/(?P<flag>\w?)')
    groups = regex.match(args.command).groupdict()
    query = re.compile(groups['query'])
    count = 0 if groups['flag'] == 'g' else 1

    for line in sys.stdin:
        print(re.sub(query, groups['replacement'], line, count=count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python implementation of UNIX sed command"
    )

    parser.add_argument('command', type=str, help='sed command')
    sed(parser.parse_args())
