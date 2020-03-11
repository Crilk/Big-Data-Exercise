#!/usr/bin/env python
from operator import itemgetter
import sys

month = 0

# input comes from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        year, month, value = line.split('\t', 2)

        # convert count (currently a string) to int
        try:
            month = int(month)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if month == 9:
            key = year + '-' + str(month)
            print('%s\t%s' % (key, value))
