import sys
sys.path.append('../')

import unittest
from  doubly_linked_list import init

class TestGetSinglyLinkedList(unittest.TestCase):
  def test_get_node_at_index_less_than_zero(self):
    dll = init(10)
    self.assertEqual(dll.get_node_at_index(-1), None)

  def test_get_node_at_index_zero(self):
    dll = init(10)
    dll.get_node_at_index(0)
    self.assertEqual(dll.head.data, 1)

  def test_get_node_at_index(self):
    dll = init(10)
    self.assertEqual(dll.get_node_at_index(5).data, 6)

if __name__ == '__main__':
    unittest.main()
