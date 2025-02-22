#!/usr/bin/env python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
  
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_another_name(self):
        testcase = "Sandra, Isiukwu"
        expected = "Isiukwu Sandra"
        self.assertEqual(rearrange_name(testcase), expected)

    def empty_test(self):
        testcase = " "
        expected = " "
        self.assertEqual((testcase), expected)

    def test_one_name(self):
        testcase = "Nnebuihe"
        expected = "Nnebuihe"
        self.assertEqual((testcase), expected)

# Run the tests
unittest.main()
