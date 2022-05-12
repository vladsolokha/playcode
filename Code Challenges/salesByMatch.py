# Given array of ints representing color of item
# Determine how many pairs of items with matching colors there are

# Function  inputs      n: number of items in pile
#                       ar[n]: colors of each item

#           outputs int: number of pairs

#!/bin/python3

def sockMerchant(n, ar):
    
    pairs = 0
    y = []
    for i in range(max(ar)):
        y.append(0)    
    for i in range(n):
        y[ar[i] - 1] += 1
    for x in y:
        if x > 1: 
            pairs += x//2

    return pairs
        
num = 9
arr = [1,2,2,1,1,3,5,1,2]

print(sockMerchant(num, arr))