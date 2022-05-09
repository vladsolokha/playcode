# arrays 
  =) read/write to index = O(1) constant
  =( add/remove/search = O(n) linear
## array methods
insert, pop, remove, index
*append = O(n)* amortized time = adding without dynamically increasing size of 
memory is O(1) constant =) but occasionally need to 
allocate more memory is O(n) linear =(

# hash tables
aka dictionary or map
  =) add/remove/search = O(1) constant
  =( amortized add operation

# sorted array
  =) binary search = O(log n) logarithmic
  =( inserting is expensive

# linked list
when you need to repeatedly add/remove elements at start or end of list
  =) add element at start or end or remove first elements = O(1) constant
  =) doubly linked list remove last element = O(n) time
  =( indexing is expensive b/c traversing list is required to index it.

# binary search tree
store elements in sorted order
  =) add/remove/search/min = O(log n) logarithmic

source: (Time complexity of array/list operations)
[https://yourbasic.org/algorithms/time-complexity-arrays/]