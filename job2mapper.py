#!/usr/bin/env python

import sys
from itertools import chain, combinations      
from collections import defaultdict

if __name__ == '__main__':

    basketList = []
    candidatePairList = []
    candidateSetFrequency = defaultdict(int)
    outputSet = dict()

    for line in sys.stdin:
        line = line.strip('\n')
        if line:
            basket = line.split()
            basketList.append(basket)

    minSup = (int)(len(basketList) * 0.005)

    candidate = open('outputCandidate.txt', 'r')

    for line in candidate:
        line = line.strip('\n')
        if line:
            candidatePair = line.split()
            candidatePairList.append(tuple(sorted([candidatePair[0],candidatePair[1]])))

    candidate.close()
    
    for basket in basketList:
        itemCombinations = chain(*[combinations(set([item for item in basket]), 2)])
        for item in itemCombinations:
            if tuple(sorted(item)) in candidatePairList:
                candidateSetFrequency[tuple(sorted(item))] += 1

    for item, freq in candidateSetFrequency.iteritems():
        if freq >= minSup:
            outputSet[tuple(sorted(item))] = freq

    for pair, freq in outputSet.iteritems():
        print pair, ".", freq