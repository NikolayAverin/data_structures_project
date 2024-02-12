"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import *


class TestLinkedList(unittest.TestCase):

    def test_str(self):
        ll = LinkedList()
        self.assertEquals(str(ll), 'None')
        ll.insert_beginning({'id': 1})
        self.assertEquals(str(ll), "{'id': 1} -> None")

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEquals(str(ll), "{'id': 0} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 1})
        self.assertEquals(str(ll), "{'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        self.assertEquals(ll.to_list(), [])
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEquals(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        # self.assertEquals(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEquals(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        with self.assertRaises(TypeError):
            ll.get_data_by_id(2)
