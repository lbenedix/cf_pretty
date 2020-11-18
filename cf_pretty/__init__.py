#!/usr/bin/env python3
import fileinput
import json
from itertools import zip_longest
import sys

from rapidtables import print_table

def main():

    json_output = '--json' in sys.argv

    lines = iter(sys.stdin.read().split('\n'))
    what = next(lines)

    header_line = next(lines)
    while len(header_line) < 10:
        header_line = next(lines)

    headers = {}
    entries = []
    for header in [x.strip() for x in header_line.split('  ') if x]:
        i = header_line.index(header)
        headers[header] = i

    result = []
    for line in lines:
        if len(line) < 1:
            continue
        if line.startswith('TIP:'):
            continue

        values = []
        for h in headers:
            x = line[headers[h]:].split('  ')[0].strip()
            values.append(x)

        new_entry = {header: value.split(', ') for header, value in zip(headers, values)}
        entries.append(new_entry)

        for current in zip_longest(*new_entry.values(), fillvalue=''):
            result.append({header: value for header, value in zip(headers, current)})

    result.append({})

    if json_output:
        print(json.dumps(entries, indent=2))
    else:
        print(what)
        print_table(result, tablefmt='md')

if __name__ == '__main__':
    main()