"""
find
"""

import argparse
import glob
import os
import subprocess
import sys


def find(args):
    if not os.path.exists(args.path):
        print('Could not find path')
        sys.exit(1)

    if not args.type in ['d', 'f']:
        print('Unknown type, use "f" or "d"')
        sys.exit(1)

    for root, dirs, files in os.walk(args.path):
        target = files if args.type == 'f' else dirs
        for name in target:
            if glob.fnmatch.fnmatch(name, args.name):
                subprocess.run([args.exec, os.path.join(root, name)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='starting directory')
    parser.add_argument('-name', type=str, required=True, help='file name glob')
    parser.add_argument('-type', type=str, default='f', help='file name glob')
    parser.add_argument('-exec', type=str, default='echo', help='unix command to call on matching files')

    args = parser.parse_args()
    find(args)

