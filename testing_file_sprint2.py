## testing file sprint 2

from us08 import *
from us12 import *
from us13 import *
from us14 import *
from us17 import *
from us18 import *

import unittest
from unittest.mock import patch
from io import StringIO
import sys

## user Story 08
class test_us08(unittest.TestCase):
	@patch.object(sys, 'argv', ['us08.py','kurt_project01.ged'])
	def test_birth_before_marriage(self):
		self.assertEqual(birth_before_marriage(), 4)

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
  
## user Story 14
class test_us14(unittest.TestCase):
	@patch.object(sys, 'argv', ['us14.py','kurt_sprint2_testfile.ged'])
	def test_multiple_sib_born(self):
		self.assertEqual(multiple_sib_born(), 0)

## user Story 17
class test_us17(unittest.TestCase):
	@patch.object(sys, 'argv', ['us17.py','kurt_us17.ged'])
	def test_no_marriages_to_descendants(self):
		self.assertEqual(no_marriages_to_descendants(), 2)
  
## user Story 18
class test_us17(unittest.TestCase):
	@patch.object(sys, 'argv', ['us18.py','kurt_us17.ged'])
	def no_marriages_to_siblings(self):
		self.assertEqual(no_marriages_to_siblings(), 0)

if __name__ == '__main__':
	unittest.main(argv=[sys.argv[0]])