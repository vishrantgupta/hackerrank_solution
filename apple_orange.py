#!/bin/python3

import sys

def appleAndOrange(s, t, a, b, apple, orange):
    # Complete this function
    
    apple_count = sum(map(lambda x : 1 if ((x + a >= s) and (x + a <= t)) else 0, apple))
    orange_count = sum(map(lambda x : 1 if ((x + b <= t) and (x + b >= s)) else 0, orange))
    
    return (apple_count, orange_count)
    

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))
