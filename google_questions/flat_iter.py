'''
Given iterator of iterators, implement interleaving iterator
input: 
arr1 = [1,2,3] as iterator1 over list
arr2 = [4,5] as iterator2 over list
arr3 = [6,7,8,9] as iterator3 over list
output:
[1,4,6,2,5,7,3,8,9]
objectives: iterators, iteration, data.struc, class, nesting
solution 1:
O(k) operations - linked list
O(1) operations, O(k) init - leave empty iterators off of iterator list
Most optimal: The Queue - it will cycle the list, when pulling item from 
iterator, check if iterator is empty, if not empty - add it back to queue
if empty, then out of elements
'''

import collections
class NoSuchElementException(Exception):
    pass
