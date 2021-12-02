## testing file sprint 4
from us21 import *
from us30 import *
from us35 import *
from us36 import *
from us37 import *
from us38 import *
from us39 import *

import unittest
from unittest.mock import patch
from io import StringIO
import sys

##User Story 21
class test_us30(unittest.TestCase):
	@patch.object(sys, 'argv', ['us30.py', 'kurt_project01.ged'])
	def test_list_married(self):
		self.assertEqual(list_married(), 1)

## user story 30
class test_us30(unittest.TestCase):
	@patch.object(sys, 'argv', ['us30.py', 'kurt_project01.ged'])
	def test_list_married(self):
		self.assertEqual(list_married(), 0)

## user story 35
class test_us35(unittest.TestCase):
	@patch.object(sys, 'argv', ['us35.py', 'kurt_us35.ged'])
	def test_recent_births(self):
		self.assertEqual(recent_births(), 1)

## user story 36
class test_us36(unittest.TestCase):
	@patch.object(sys, 'argv', ['us35.py', 'kurt_us36.ged'])
	def test_recent_deaths(self):
		self.assertEqual(recent_deaths(), 2)

## user story 37
class test_us37(unittest.TestCase):
	@patch.object(sys, 'argv', ['us37.py', 'kurt_sprint4_testfile.ged'])
	def test_recent_survivors(self):
		self.assertEqual(recent_survivors(), 5)

## user story 38
class test_us38(unittest.TestCase):
	@patch.object(sys, 'argv', ['us38.py', 'kurt_sprint4_testfile.ged'])
	def test_upcoming_birthdays(self):
		self.assertEqual(upcoming_birthdays(), 0)


## user story 39
class test_us42(unittest.TestCase):
	@patch.object(sys, 'argv', ['us39.py',  'kurt_sprint4_testfile.ged'])
	def test_list_upcoming_anniversaries(self):
		self.assertEqual(list_upcoming_anniversaries(), 1)

## user story 42
class test_us42(unittest.TestCase):
	@patch.object(sys, 'argv', ['project03.py', 'TaylorGED.ged'])
	def test_get_info(self):
		self.assertEqual(get_info('TaylorGED.ged'), 0)


if __name__ == '__main__':
	unittest.main(argv=[sys.argv[0]])