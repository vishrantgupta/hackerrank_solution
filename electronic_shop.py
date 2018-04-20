#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    
    import itertools as it
    l = sorted(list(map(sum, list(it.product(keyboards, drives)))), reverse=True)
    
    for val in l:
        if s > val or s == val:
            return val
    return -1
    

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
