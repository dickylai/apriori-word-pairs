#!/usr/bin/env python

import sys
from collections import defaultdict

if __name__ == '__main__':

    outputSet = dict()
    candidatePairFrequency = defaultdict(int)

    minSup = 4725

    for line in sys.stdin:
        line = line.strip("\n") 
        if line:
            pair, count = line.split(" . ")
            candidatePairFrequency[pair] += int(count)
    
    for pair, freq in candidatePairFrequency.iteritems():
        if freq >= minSup:
            outputSet[pair] = freq

    for pair, freq in outputSet.iteritems():
        print pair, freq