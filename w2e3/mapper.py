#!/usr/bin/env python
import sys
import os

# get input file name
input_name = os.environ['mapreduce_map_input_file']

# using name of input file figure out if airport is Heathrow or Wick
# store this information as a loc = H or loc = W
if 'heathrow' in input_name:
    loc = 'H'
else:
    loc = 'W'

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # if line contains 'yyyy' in it remove it (it is header line)
    if 'yyyy' in line:
        continue

    # split line into year, month, tmax, tmin and rain variables
    year, month, tmax, tmin, rain = line.split()

    # create key to be 'year-month-loc'
    key = '%s-%s-%s' % (year, month, loc)

    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited;
    print('%s\t%s\t%s\t%s' % (key, tmax, tmin, rain))
