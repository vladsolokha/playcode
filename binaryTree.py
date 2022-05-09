import queue


class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insLeft(self, value):
    if self.left is None:
      self.left = BinaryTree(value)
    nnode = BinaryTree(value)
    nnode.left = self.left
    self.left = nnode

  def insRight(self, value):
    if self.right is None:
      self.right = BinaryTree(value)
    nnode = BinaryTree(value)
    nnode.right = self.right
    self.right = nnode

  # traverse through root, left, right
  def dfs_pre_order(self):
    print(self.value)
    if self.left:
      self.left.dfs_pre_order()
    if self.right:
      self.right.dfs_pre_order()
  # traverse through left, middle, right
  def dfs_in_order(self):
    if self.left:
      self.left.bfs_in_order()
    print(self.value)
    if self.right:
      self.right.bfs_in_order()
  # traverse through left, right, middle
  def dfs_post_order(self):
    if self.left:
      self.left.dfs_post_order()
    if self.right:
      self.right.dfs_post_order()
    print(self.value)
  
  def bfs_queue(self):
    queue = Queue()
    queue.put(self)

    while not queue.empty():
      current = queue.get()
      print(current.value)

      if current.left:
        queue.put(current.left)
      if current.right:
        queue.put(current.right)

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  def ins(self, value):
    if value <= self.value and self.left:
      self.left.ins(value)
    elif value <= self.value:
      self.left = BinarySearchTree(value)
    elif value >= self.value and self.right:
      self.right.ins(value)
    elif value >= self.value:
      self.right = BinarySearchTree(value)
  '''if value of new node (value) is > current node (self.value),
  go to right subtree, if empty insert, if there is right child make insert new value for whole tree.
  if value of new node (value) is < current node (self.value), 
  go to left subtree. if self.value doesn't have left child insert value. 
  if left subtree self.value (current node) has left child, insert as new value for BinarySearchTree. 
  '''
  def search(self, value):
    if value < self.value and self.left:
      return self.left.search(value)
    if value > self.value and self.right:
      return self.right.search(value)
    return value == self.value
  '''if value is less than node and there is a left child go to left child and do search again.
  if value is greater than node and there is a right child go to right child and do search again with right child. 
  until value is equal to self.value
  '''
  def remove_node(self, value, parent):
    '''
    if node has no children
      simply delete, no reorganization needed
      see 2nd elif and 4th elif of first half of ifs
    if node has one child -- left or right
      parent of value points to child node
      if value is left child, parent of left child points to child
      if value is right child, parent of right child points to child
    if node has 2 child
      min node gets swapped with value to be removed
    '''
    if value < self.value and self.left:
        return self.left.remove_node(value, self)
    elif value < self.value:
        return False
    elif value > self.value and self.right:
        return self.right.remove_node(value, self)
    elif value > self.value:
        return False
    else:
        # node with no children on left
        if self.left is None and self.right is None and self == parent.left:
            parent.left = None
            self.clear() # Set all values to None
        # node with no children on right
        elif self.left is None and self.right is None and self == parent.right:
            parent.right = None
            self.clear() # Set all values to None
        # node with left child on parent left no right child
        elif self.left and self.right is None and self == parent.left:
            parent.left = self.left
            self.clear()
        # node with right child on parent right no right child
        elif self.left and self.right is None and self == parent.right:
            parent.right = self.left
            self.clear()
        # node with right child on parent left no left child
        elif self.right and self.left is None and self == parent.left:
            parent.left = self.right
            self.clear()
        # node with right child on parent right no left child
        elif self.right and self.left is None and self == parent.right:
            parent.right = self.right
            self.clear()
        else: # 2 children, find min and replace right child with value
            self.value = self.right.min()
            self.right.remove_node(self.value, self)
        return True
  def clear(self):
    self.value = None
    self.left = None
    self.right = None
  def min(self):
    if self.left:
      return self.left.min()
    return self.value
    