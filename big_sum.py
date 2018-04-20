#!/bin/python3

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    
    if n == 1:
        return ar[0]
    
    return ar[n - 1] + aVeryBigSum(n - 1, ar)
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
