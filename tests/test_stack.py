"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEquals(stack.top.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEquals(stack.top.data, 'data1')
        self.assertEquals(data, 'data2')

    def test_str(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEquals(stack.__str__(), 'data2')
