#!/bin/python3

import sys
import itertools as it

def divisibleSumPairs(n, k, ar):
    # Complete this function
    l = list(it.combinations(ar, 2))

    return sum(list(map(lambda x : 1 if sum(x) % k == 0 else 0, l)))

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
