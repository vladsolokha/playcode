#given unordered array, consists of consecutive int without duplicates
#swap any 2 elements
#find min number of swaps req to sort array in ascending order

'''
example: 
arr = [7,1,3,2,4,5,6] perform the steps

i   arr             swap    (indicies)
0   [7,1,3,2,4,5,6] swap    (0,3)
1   [2,1,3,7,4,5,6] swap    (0,1)
2   [1,2,3,7,4,5,6] swap    (3,4)
3   [1,2,3,4,7,5,6] swap    (4,5)
4   [1,2,3,4,5,7,6] swap    (5,6)
5   [1,2,3,4,5,6,7] 

it took 6 swaps to sort the array
'''

sam1 = [4,3,1,2] #returns 3
sam2 = [2,3,4,1,5] #returns 3
sam3 = [1,3,5,2,4,6,7] #returns 3

def minimumSwaps(arr):
    pass


for swap in (sam1,sam2,sam3):
    minimumSwaps(swap)

