class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
  def __repr__(self):
    return self.data

class LinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for i in nodes:
        node.next = Node(data=i)
        node = node.next
  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.data)
      node = node.next
    nodes.append("None")
    return " --> ".join(nodes)
  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next
  def __getitem__(self, key):
    node = self.head
    while node is not None:
      if key == node:
        return 
      node = node.next
  def add(self, node):
    node.next = self.head
    self.head = node
  def append(self, node):
    if self.head is None:
      self.head = node
      return
    for current_node in self:
      pass
    current_node.next = node
  def insert(self, target, new_node):
    if self.head is None:
      return self.add(new_node)
    for node in self:
      if node.data == target:
        new_node.next = node.next
        node.next = new_node
        return
    raise Exception("Node with data '%s' not found" % target)
  def remove(self, goal):
    if self.head is None:
      raise Exception("List is empty")
    # check if head is goal node to remove
    if self.head.data == goal:
      # assign next node to head if head was goal
      self.head = self.head.next
      return
    # assign head to prev node var
    prev_node = self.head
    for node in self:
      if node.data == goal:
        prev_node.next = node.next
        return
      prev_node = node
    raise Exception("Node with data '%s' not found" % goal)
  def get(self, goal):
    if self.head is None:
      raise Exception("List is empty")
    if self.head.data == goal:
      return
    for node in self:
      if node.data == goal:
        return
    raise Exception("Node with data '%s' not found" % goal)
  def reverse(self):
    if self.head is None:
      raise Exception("List is empty")
    prev = None
    current = self.head
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
