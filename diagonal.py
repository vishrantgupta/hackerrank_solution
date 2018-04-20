#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    count = 0
    sum_t = 0
    
    for e in a:
        sum_t = sum_t + e[count] - e[len(e) - count - 1]
        count = count + 1
    
    return abs(sum_t)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
