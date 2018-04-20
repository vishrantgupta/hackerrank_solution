#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    
    del ar[k]
    
    total = sum(ar)
    
    if total / 2 == b:
        return "Bon Appetit"
    else:
        return int(abs((total / 2) - b))

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
