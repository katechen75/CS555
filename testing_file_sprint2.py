## testing file sprint 2

from us12 import *
from us13 import *

import unittest
from unittest.mock import patch
from io import StringIO
import sys

## user Story 12
class test_us12(unittest.TestCase):
	@patch.object(sys, 'argv', ['us12.py','kurt_sprint2_testfile.ged'])
	def test_parents_not_too_old(self):
		self.assertEqual(parents_not_too_old(), 4)

## user Story 13
class test_us13(unittest.TestCase):
	@patch.object(sys, 'argv', ['us13.py','kurt_sprint2_testfile.ged'])
	def test_siblings_age_diff(self):
		self.assertEqual(sibling_age_diff(), 1)

if __name__ == '__main__':
	unittest.main(argv=[sys.argv[0]])