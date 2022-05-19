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

# Use cases for data structures
## (doubly) Linked List
properties - store seq data that can grow/shrink in O(1) time
at expense of random access (bad for search)
applications - queue 

## Graph
properties - models a network of objects
each has some connection to zero or more of the same type of object
applications - social network, friends are edges of a vertex account. Answer ? about relationships b/w users using graph algos. Want to know if Bob is friend of friend of Jim? Run BFS with max depth 2 and see if there's a path b/w them. Use data from graph to help suggest friends, insights for ads, etc

## Binary Search Tree (BST)
properties - store orderable data which can be retrieved O(log n) time. Traverse in sorted order.
applications - store users currently online in chat app. Get names in sorted order and search through names to find if specific user is online

## AVL or other Self-Balancing Binary Trees
properties - store and insert orderable data.
If tree becomes unbalanced, rotate it so it remains balanced for optimal search

## Trie-tree
properties - store and insert words or phrases into tree.
Easily find common words
application - autocorrect, spell check suggestions, code suggestions
