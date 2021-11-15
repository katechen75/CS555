## testing file sprint 3

from us27 import *
from us29 import *

import unittest
from unittest.mock import patch
from io import StringIO
import sys

## user Story 27
class test_us27(unittest.TestCase):
	@patch.object(sys, 'argv', ['us27.py','kurt_project01.ged'])
	def test_include_individual_ages(self):
		self.assertEqual(include_individual_ages(), 37)

## user Story 29
class test_us29(unittest.TestCase):
	@patch.object(sys, 'argv', ['us29.py','kurt_project01.ged'])
	def test_list_deceased(self):
		self.assertEqual(list_deceased(), 19)

if __name__ == '__main__':
	unittest.main(argv=[sys.argv[0]])