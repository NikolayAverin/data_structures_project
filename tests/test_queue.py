"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import *


class TestQueue(unittest.TestCase):
    def test_str(self):
        queue = Queue()
        self.assertEquals(str(queue), "")
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEquals(str(queue), "data1\ndata2")

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEquals(queue.head.data, 'data1')
        self.assertEquals(queue.head.next_node.data, 'data2')
        self.assertEquals(queue.tail.data, 'data3')
        self.assertEquals(queue.tail.next_node, None)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEquals(queue.dequeue(), 'data1')
        self.assertEquals(queue.dequeue(), 'data2')
        self.assertEquals(queue.dequeue(), 'data3')
        self.assertEquals(queue.dequeue(), None)
