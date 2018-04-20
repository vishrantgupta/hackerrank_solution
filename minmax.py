import sys


def miniMaxSum(arr):
    # Complete this function
    
    total = sum(arr)
    min_l = min(arr)
    max_l = max(arr)
    
    print(total - max_l, total - min_l)
    
    
    
    

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

