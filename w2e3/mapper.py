#!/usr/bin/env python
import sys
import os

filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    key = words[0] + '-' + words[1]
    value = words[2] + ',' + words[3] + ',' + words[4]

    print('%s\t%s\t%s' % (key, value, filename))
