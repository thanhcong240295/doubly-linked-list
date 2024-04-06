import sys
sys.path.append('../')

import unittest
from  doubly_linked_list import init

class TestInsertDoublyLinkedList(unittest.TestCase):
  def test_insert_at_head(self):
    dll = init(10)
    dll.insert_at_head(11)
    self.assertEqual(dll.head.data, 11)

  def test_insert_at_tail_list_empty(self):
    dll = init(0)
    dll.insert_at_tail(11)
    
    current = dll.head
    
    while current.next:
       current = current.next

    self.assertEqual(dll.head.data, 11)
    self.assertEqual(current.data, 11)

  def test_insert_at_tail(self):
    dll = init(10)
    dll.insert_at_tail(11)
    
    current = dll.head
    
    while current.next:
       current = current.next

    self.assertEqual(dll.head.data, 1)
    self.assertEqual(current.data, 11)

  def test_insert_at_index_lester_than_zero(self):
    dll = init(10)
  
    self.assertEqual(dll.insert_at_index(11, -1), None)

  def test_insert_at_index_zero(self):
    dll = init(10)
    dll.insert_at_index(11, 0)

    self.assertEqual(dll.head.data, 11)

  def test_insert_at_index_grater_than_len(self):
    dll = init(10)
    dll.insert_at_index(20, 20)

    current = dll.head

    while current.next:
       current = current.next

    self.assertEqual(dll.head.data, 1)
    self.assertEqual(current.data, 10)

  def test_insert_at_index(self):
    dll = init(10)
    dll.insert_at_index(20, 5)

    self.assertEqual(dll.get_node_at_index(4).data, 5)
    self.assertEqual(dll.get_node_at_index(5).data, 20)
    self.assertEqual(dll.get_node_at_index(6).data, 6)

if __name__ == '__main__':
    unittest.main()
