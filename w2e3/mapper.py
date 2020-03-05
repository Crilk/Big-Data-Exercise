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
    for index in range(0, int(len(words) / 5)):
        key = words[index * 5] + '-' + words[index * 5 + 1]
        value = words[index * 5 + 2] + '-' + words[index * 5 + 3] + '-' + words[index * 5 + 4]

        print('%s\t%s\t%s' % (key, value, filename))
