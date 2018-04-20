#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    # 12:40:22AM
    # s = "06:40:03AM"
    time = s.split(":", 1)
    
    hr = int(time[0])
    
    if hr == 12:
        hr = 0
    
    if time[1][-2] == 'P':
        return str(hr + 12) + ":" + time[1][0:-2]
    else:
        if hr < 10:
            return "0" + str(hr) + ":" + time[1][0:-2]
        return str(hr) + ":" + time[1][0:-2]
        

s = input().strip()
result = timeConversion(s)
print(result)
