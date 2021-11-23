## testing file sprint 4
from us37 import *
from us38 import *

import unittest
from unittest.mock import patch
from io import StringIO
import sys


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

if __name__ == '__main__':
	unittest.main(argv=[sys.argv[0]])