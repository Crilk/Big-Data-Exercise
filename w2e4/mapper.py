#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line by empty space
    key, value = line.split('\t', 1)
    # split the line by -
    year, month = key.split('-', 1)

    print('%s\t%s\t%s\t' % (year, month, value))
