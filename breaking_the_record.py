#!/bin/python3

import sys

def breakingRecords(score):
    # Complete this function
    if len(score) > 0:
        
        max_score = set()
        max_record = score[0]
                
        # min_score = set(score[1:])
        min_score = set()
        min_record = score[0]
        
        for x in score:
            if x > max_record:
                max_score.add(x)
                max_record = x
            elif x < score[0] and x < min_record:
                min_score.add(x)
                min_record = x
        
        # min_score = [x for x in (min_score - max_score) if x < score[0]]
        
        return (len(max_score), len(min_score))

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


