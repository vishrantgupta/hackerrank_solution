#!/bin/python3

import sys

def plusMinus(arr):
    
    a_len = len(arr)
    
    if(a_len == 0):
        return
    
    # Complete this function
    positive = 0
    negative = 0
    zero = 0
    
    for element in arr:
        if element > 0:
            positive = positive + 1
        elif element < 0 :
            negative = negative + 1
        else:
            zero = zero + 1
     
    print(positive / a_len)
    print(negative / a_len)
    print(zero / a_len)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
