#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    # map, count, occurance, occurrence
    ar = [(x,ar.count(x)) for x in set(ar)]
    
    from operator import itemgetter
    
    return max(ar, key = itemgetter(1))[0]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
