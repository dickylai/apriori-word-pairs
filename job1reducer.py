#!/usr/bin/env python

import sys  

if __name__ == '__main__':

    outputSet = set()

    for line in sys.stdin:
        line = line.strip("\n") 
        if line:
            pair = line.split()
            outputSet.add(tuple(sorted([pair[0],pair[1]])))

    for first, second in outputSet:
        print first, second