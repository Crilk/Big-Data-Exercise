#!/usr/bin/env python
from operator import itemgetter
import sys

# print header line
print('yyyy\tmm\tHtmax\tHtmin\tHrain\tWtmax\tWtmin\tWrain')

current_date = None
current_loc = None
current_output = None
date = None
loc = None
test = 0  # this variable is to keep track if we have come to times when both H and W $

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, tmax, tmin, rain = line.split()

    # split key into year, month and location
    year, month, loc = key.split('-')

    # create date
    date = '%s-%s' % (year, month)

    # this If-switch only works because Hadoop sorts map output
    # by key (here year-month-loc) before it is passed to the reducer
    if current_date == date:
        # this means data for both airports exists for this date
        # write results to STDOUT
        print('%s\t%s\t' % (year, month) + current_output + '\t%s\t%s\t%s' % (tmax, tmin, rain))

        # update current data
        current_date = date
        current_loc = loc
        current_output = '%s\t%s\t%s' % (tmax, tmin, rain)

        # Set test variable to 1 so that same data is not printed twice
        test = 1
    else:
        # this means that the new date is different from previous
        # need to figure out if this is a change from W to W or from W to H
        if current_loc == loc:
            # this means we have a change from W to W i.e. no H data is p$
            # write results to STDOUT
            print('%s\t%s\t-\t-\t-\t' % (current_date.split('-')[0], current_date.split('-')[1]))

            # update current data
            current_loc = loc
            current_date = date
            current_output = '%s\t%s\t%s' % (tmax, tmin, rain)
        else:
            # current_loc is empty so set up current data
            current_loc = loc
            current_date = date
            current_output = '%s\t%s\t%s' % (tmax, tmin, rain)
