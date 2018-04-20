#!/bin/python3

import sys

def getTotalX(a, b):
    # Complete this function

    max_a = max(a)
    min_b = min(b)
    
    vals = list(range(max_a, min_b + 1))

    for i in a:
        vals = [x for x in vals if x % i == 0]
    
    for i in b:
        vals = [x for x in vals if i % x == 0]

    return len(vals)
    
    
def lcm(a, b):
    m = max(a,b)
    while True:
        if m % a == 0 and m % b == 0:
            return m
        m += 1


    

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
