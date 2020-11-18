#!/usr/bin/env python3
import fileinput
import json
from itertools import zip_longest
from subprocess import check_output

from rapidtables import print_table

if __name__ == '__main__':

    lines = fileinput.input()
    what = next(lines).split(' ')[1]

    header_line = next(lines)
    while len(header_line) < 10:
        header_line = next(lines)

    headers = {}
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

        for current in zip_longest(*new_entry.values(), fillvalue=''):
            result.append({header: value for header, value in zip(headers, current)})

    result.append({})

    print_table(result, tablefmt='md')
