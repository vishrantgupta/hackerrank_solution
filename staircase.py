#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    
    i = 0
    while (i < n):
        print((n - i - 1) * " ", end= "")
        print("#" * (i + 1))
        i = i + 1

        
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
