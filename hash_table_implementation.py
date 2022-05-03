#Implement dictionary style hash table
# from  https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd

# Should be prime and able to be changed
INITIAL_CAPACITY = 50

# Node is a structure like a linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    # represent the node object as a string
    def __str__(self):
        return 'Node: (%s, %s), next: %s' % (self.key, self.value, self.next != None)
    def __repr__(self):
        return str(self)

# HashTable Node
class HashTable:
    # Initialize has table
    def __init__(self):
        self.capacity = INITIAL_CAPACITY 
        self.size = 0 # Number of elements inserted into internal array.
        self.buckets = [None] * self.capacity
        # internal array, storing each inserted value in
        # a bucket based on provided key
    '''Next means hashtable is part of linked list
    hashtable uses separate chaining where each bucket
    conains linkedlist of nodes containing the objects
    stored at that index, this is one method of collision resolution
    '''

    # Methods of
    # Hash
    '''take the key(string of any length) and produce 
    index for internal buckets array. create a hash function
    to convert string to index. Need our function to be uniform
    across buckets to avoid collisions of keys. 
    '''
    def hash(self, key):
        hashsum = 0
        # For each character in the key

        for index, current in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (index + len(key)) ** ord(current)
            # Perform modulus to keep hashsum in range of [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

    # Insert
    '''insert key/value pair into hash table
    1. increment size of hash table
    2. compute index of key using hash function above
    3. if bucket at index is empty, create new node and add it there
    4. else a collision occured, there's already linked list of at least one node at the index. Iterate to end of list and add new node there
    '''
    def insert(self, key, value):
        # Increment size
        self.size += 1
        # Compute index of key
        index = self.hash(key)
        # Go to node linked to hash
        node = self.buckets[index]
        # If bucket empty
        if node is None:
            # Create node, add, return
            print('bucket is none')
            self.buckets[index] = Node(key, value)
            return 
        # Collision? Iterate to end of linked list at index
        prev = node
        while node is not None:
            prev=node
            node = node.next
        # Add new node at end of list with provided key/val
        prev.next = Node(key, value)

    # Find
    '''retrieving data from hash table
    1. compute index for provided key using hash function
    2. go to bucket for that index
    3. iterate the nodes in linked list until key is found or end of list is reached
    4. return value of found node or None if found
    '''
    def find(self, key):
        # compute hash (same as line 57)
        index = self.hash(key)
        # go to first node in list at bucket
        node = self.buckets[index]
        # traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # now, node is requested key/val pair or None
        if node is None:
            # not found
            print('did not find value for: ', key)
            return None
        else: 
            # found - return the data value
            print('value is: ', node.value)
            return node.value
    
    # Remove
    '''
    1. Compute hash for key to determine index
    2. Iterate linked list of nodes. Continue until end of list or key is found.
    3. If key is not found return None
    4. else remove node from linked list and return node value. 
    '''
    def remove(self, key):
        # compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        # iterate on requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # now node is either requested node or none
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            # delete this element in linked list
            if prev is None:
                print('did not find value for: ', key)
                node = None
            else: 
                prev.next = prev.next.next
            # return the deleted language
            return result
    def look(self):
        return self.buckets[index]
'''
Applications 
Hash tables solve:
1. write a function to determine whether string has repeated characters
2. given string of any length, find most-used character in the string
3. write a function to determine whether two strings are anagrams
'''