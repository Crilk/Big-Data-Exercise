#!/usr/bin/env python
from operator import itemgetter
import sys

current_key = None
current_value = None
current_label = None
key = None

# input comes from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from mapper.py
        key, value, label = line.split('\t', 2)
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_key == key:
            if label == "wickairportdata.txt":
                current_value = current_value + '|' + value
            elif label == "heathrowdata.txt":
                current_value = value + '|' + current_value
        else:
            if current_key:
                # write result to STDOUT
                print('%s\t%s' % (current_key, current_value))
            current_value = value
            current_key = key

# do not forget to output the last word if needed!
if current_key == key:
    print('%s\t%s' % (current_key, current_value))
