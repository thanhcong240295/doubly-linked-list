class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self) -> None:
    self.head = None

  def insert_at_head(self, data: int):
    new_node = Node(data)
    new_node.prev = None
    new_node.next = self.head

    if (self.head):
      self.head.prev = new_node

    self.head = new_node
  
  def insert_at_tail(self, data: int):
    if (self.head is None):
      return self.insert_at_head(data)
    
    node_len = self.get_len()
    prev_node = self.get_node_at_index(node_len - 1)

    new_node = Node(data)
    new_node.prev = prev_node
    new_node.next = None

    prev_node.next = new_node

  def insert_at_index(self, data: int, index: int):
    node_len = self.get_len()

    if (index < 0 or index > node_len):
      return None

    if (index == 0):
      return self.insert_at_head(data)

    if (index == node_len - 1):
      return self.insert_at_tail(data)
    
    prev_node = self.get_node_at_index(index - 1)
    
    new_node = Node(data)
    new_node.prev = prev_node
    new_node.next = prev_node.next

    prev_node.next = new_node

  def delete_first_node(self):
    node_len = self.get_len()
    if (node_len == 0):
      return None

    if (node_len == 1):
      self.head = None
      return self.head

    next_node = self.head.next
    next_node.prev = None
    self.head = next_node

  def delete_last_node(self):
    node_len = self.get_len()
    if (node_len == 0 or node_len == 1):
      return self.delete_first_node()
    
    prev_node = self.get_node_at_index(node_len - 2)
    prev_node.next = None

  def delete_node_at_index(self, index: int):
    node_len = self.get_len()
    if (index < 0 or index >= node_len):
      return None

    if (index == 0):
      return self.delete_first_node()

    if (index == node_len - 1):
      return self.delete_last_node()
    
    node_delete = self.get_node_at_index(index)

    node_delete.prev.next = node_delete.next
    node_delete.next.prev = node_delete.prev

  def get_node_at_index(self, index: int):
    node_len = self.get_len()

    if (index < 0 or index > node_len):
      return None

    if (index == 0):
      return self.head
    
    current = self.head
    for i in range(0, index):
      current = current.next

    return current

  def get_len(self) -> int:
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  def display(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next

def init(len: int):
  sll = DoublyLinkedList()

  for i in range(0, len):
    sll.insert_at_tail(i + 1)

  return sll