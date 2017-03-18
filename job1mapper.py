#!/usr/bin/env python

import sys
from itertools import chain, combinations      
from collections import defaultdict

if __name__ == '__main__':

    basketList = []
    freqSet = set()
    itemSet = defaultdict(int)
    candidateSetFrequency = defaultdict(int)
    outputSet = dict()

    for line in sys.stdin:
        line = line.strip('\n')
        if line:
            basket = line.split()
            basketList.append(basket)

    minSup = (int)(len(basketList) * 0.005)
    
    for basket in basketList:
        itemCombinations = chain(*[combinations(basket, 1)])
        for item in itemCombinations:
            itemSet[tuple(item)] += 1

    for item, count in itemSet.iteritems():
        if count >= minSup:
            freqSet.add(item)

    for basket in basketList:
        itemCombinations = chain(*[combinations(set([item for item in basket if tuple([item]) in freqSet]), 2)])
        for item in itemCombinations:
            candidateSetFrequency[tuple(sorted(item))] += 1

    for item, freq in candidateSetFrequency.iteritems():
        if freq >= minSup:
            outputSet[tuple(sorted(item))] = freq

    for first, second in outputSet:
        print first, second