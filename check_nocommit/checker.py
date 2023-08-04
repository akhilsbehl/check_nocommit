import argparse
import re
import sys
from typing import List, Tuple

import git


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    return parser.parse_args()


def check_for_nocommit(filename: str) -> List[Tuple[int, str]]:
    results = []
    with open(filename) as file:
        in_nocommit_block = False
        for i, line in enumerate(file, start=1):
            if re.search(r"# NOCOMMIT:START", line):
                in_nocommit_block = True
            if re.search(r"# NOCOMMIT:END", line):
                in_nocommit_block = False
            if re.search(r"# NOCOMMIT", line) or in_nocommit_block:
                results.append((i, line.strip()))
    return results


def main() -> int:
    args = parse_args()

    filenames = args.filenames if args.filenames else []

    any_nocommit_found = False
    for filename in filenames:
        if filename.endswith('.py') or filename.endswith('.sh'):
            results = check_for_nocommit(filename)
            if results:
                any_nocommit_found = True
            for line_number, line in results:
                print(f'NOCOMMIT:{filename}:{line_number}: {line}')

    return int(any_nocommit_found)


if __name__ == '__main__':
    sys.exit(main())
