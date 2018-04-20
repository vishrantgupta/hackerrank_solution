#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    
    if not ar:
        return 0
    
    max_l = ar[0]
    count = 1
    
    for i in ar[1:]:
        if i > max_l:
            max_l = i
            count = 1
        elif i == max_l:
            count = count + 1
    
    return count
    
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
