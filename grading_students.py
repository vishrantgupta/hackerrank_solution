#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    
    for i, grade in enumerate(grades):
        
        if grade < 38:
            continue
        
        remainder = 10 - (grade % 10)
        
        if (remainder < 3 and remainder > 0):
            grades[i] = grade + remainder
            
        if (remainder > 5 and remainder < 8):
            grades[i] = grade + remainder - 5
            
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
