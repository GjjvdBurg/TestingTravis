# -*- coding: utf-8 -*-

from testpackage import func

import unittest

class TestCase(unittest.TestCase):

    def test_func(self):
        exp = "Hello, World!"
        out = func()
        self.assertEqual(exp, out)

    def test_func_2(self):
        self.assertTrue(False)
