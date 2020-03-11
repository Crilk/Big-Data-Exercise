#!/usr/bin/env python
import sys
import os

doneFirst = 0
filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # ignore the first line of data (the header line)
    if doneFirst == 0:
        doneFirst = 1
        continue

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    key = words[0] + '-' + words[1]
    value = words[2] + ',' + words[3] + ',' + words[4]

    print('%s\t%s\t%s' % (key, value, filename))
