#!/bin/python3

import sys

def solve(year):
    # Complete this function
    
    days, nextMonth = sumDays(year);
    
    date = getDayOfProgrammer() - days

    return str(date) + "." + nextMonth + "." + str(year)
    
def getDayOfProgrammer():
    return 256;
    
def sumDays(year):
    
    months = [("01",31), ("02",28), ("03",31), ("04",30), ("05",31), ("06",30), ("07",31), ("08",31), ("09",30), ("10",31), ("11",30), ("12",31)]
    
    days = 0
    nextMonth = ""
    
    if isLeapYear(year):
        days += 1
    
    for key in months:
        
        if (days + key[1] > getDayOfProgrammer()):
            nextMonth = key[0]
            break
        
        days += key[1]
    
    if year == 1918:
        days = days - 13
    
    return (days, nextMonth)
        
    
    
def isLeapYear(year):
    
    if year < 1918:
        return True if year % 4 == 0 else False
    
    if year % 400 == 0:
        return True
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    return False

year = int(input().strip())
result = solve(year)
print(result)
