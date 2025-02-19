#!/usr/bin/env python3

import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
  
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_another_self(self):
        testcase = "Sandra Isiukwu"
        expected = "Isiukwu Sandra"
        self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
unittest.main()
