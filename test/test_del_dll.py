import sys
sys.path.append('../')

import unittest
from  doubly_linked_list.doubly_linked_list import init

class TestDeleteDoublyLinkedList(unittest.TestCase):
  def test_delete_first_node_list_empty(self):
    dll = init(0)
    dll.delete_first_node()
    self.assertEqual(dll.delete_first_node(), None)

  def test_delete_first_node_only_one(self):
    dll = init(1)
    dll.delete_first_node()
    self.assertEqual(dll.get_len(), 0)
    self.assertEqual(dll.head, None)

  def test_delete_first_node(self):
    dll = init(10)
    dll.delete_first_node()
    self.assertEqual(dll.get_len(), 9)
    self.assertEqual(dll.head.data, 2)

  def test_delete_last_node_list_empty(self):
    dll = init(0)
    dll.delete_last_node()
    self.assertEqual(dll.delete_first_node(), None)

  def test_delete_last_node_only_one(self):
    dll = init(1)
    dll.delete_last_node()
    self.assertEqual(dll.get_len(), 0)
    self.assertEqual(dll.head, None)

  def test_delete_last_node(self):
    dll = init(10)
    dll.delete_last_node()
    self.assertEqual(dll.get_len(), 9)
    self.assertEqual(dll.get_node_at_index(8).next, None)

  def test_delete_node_at_index_list_empty(self):
    dll = init(0)
    self.assertEqual(dll.delete_node_at_index(1), None)

  def test_delete_node_at_index_index_less_than_zero(self):
    dll = init(10)
    self.assertEqual(dll.delete_node_at_index(-1), None)
    self.assertEqual(dll.get_len(), 10)

  def test_delete_node_at_index_index_less_zero(self):
    dll = init(10)
    dll.delete_node_at_index(0)
    self.assertEqual(dll.head.data, 2)
    self.assertEqual(dll.get_len(), 9)

  def test_delete_node_at_index_index_greater_than_list_len(self):
    dll = init(10)
    self.assertEqual(dll.delete_node_at_index(20), None)

  def test_delete_node_at_index_index(self):
    dll = init(10)
    dll.delete_node_at_index(5)
    self.assertEqual(dll.get_node_at_index(4).data, 5)
    self.assertEqual(dll.get_node_at_index(5).data, 7)

if __name__ == '__main__':
    unittest.main()
