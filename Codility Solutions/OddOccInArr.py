def solution(A):
    # use hash table to keep track of frequency of each occuring value
    # O(n) time and space
    # one traversal
    # create empty dictionary
    # traverse the array
    # if key exists in dictionary
    #   delete the key
    # otherwise add 1 as value to key
    # dictionary will contain the only unpaired value
    # return the key
    d = {}
    for num in A:
        if num in d:
            d.pop(num)
        else: 
            d[num] = 1
    for k, v in d.items():
        if v == 1:
            return k

'''User test case 1:
[3, 5, 4, 5, 6, 7, 1, 23, 5, 2, 79, 3, 4, 7, 23, 79, 5, 1, 2]
User test case 2:
[1, 2, 1]
'''