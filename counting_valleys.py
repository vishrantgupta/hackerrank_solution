#!/bin/python3

import sys

def countingValleys(n, s):
    # Complete this function
    
    groundLevel = 0
    valleyCount = 0
    flag = False
    
    for val in s:
        if val == 'U':
            groundLevel += 1
            if groundLevel > 0 or groundLevel == 0:
                flag = False
            
        else:
            groundLevel -= 1
            if groundLevel < 0 and not flag:
                flag = True
                valleyCount += 1
     
    return valleyCount
                

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
