#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    
    # socks = {}
    # for sock in ar:
    #    if sock not in socks:
    #        socks[sock] = 1
    #    else:
    #        socks[sock] += 1
    #    
    # count = 0
    #   
    # for key, value in socks.items():
    #    count += int(value / 2)
    
    # socks = [int(ar.count(x) / 2) for x in set(ar)]
    # count = sum(socks)
    # return count
    
    return sum(map(lambda x: int(ar.count(x) / 2), set(ar)))
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
