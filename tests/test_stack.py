"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEquals(stack.top.data, 'data1')
