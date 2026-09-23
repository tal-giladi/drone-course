# -*- coding: utf-8 -*-
"""Repair print(" lines that got a real newline instead of a \\n escape.

Bash heredocs and `py -c` both eat backslashes; this puts them back.
Usage: py fixnl.py <file.py>
"""
import io
import sys

BS = chr(92)

path = sys.argv[1]
lines = io.open(path, encoding='utf-8').read().split('\n')
out, i, n = [], 0, 0
while i < len(lines):
    if lines[i].rstrip().endswith('print("') and i + 1 < len(lines):
        head = lines[i].rstrip()[:-1]        # drop the dangling quote
        out.append(head + '"' + BS + 'n' + lines[i + 1].lstrip('\r'))
        i += 2
        n += 1
        continue
    out.append(lines[i])
    i += 1
io.open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('repaired', n, 'line(s) in', path)
