#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    
    if x1 < x2 and v2 < v1:
        
        while (x1 < x2):
            
            x1 = x1 + v1
            x2 = x2 + v2
        
    elif x2 < x1 and v1 < v2:
        
        while (x2 < x1):
            
            x1 = x1 + v1
            x2 = x2 + v2

    return "YES" if x1 == x2 else "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
