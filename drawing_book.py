#!/bin/python3

import sys

def solve(n, p):
    # Complete this function
    
    # n = total number of pages in a book
    # p = required page
    if p - 1 < n - p:
        return int(p / 2)
    else:
        return int((n- (p if p%2 == 0 else p - 1)) / 2)
    
    

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
