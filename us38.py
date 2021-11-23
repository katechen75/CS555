# Author: Kurt von Autenried

# Code for User Story 38

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def upcoming_birthdays():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for individual in info['individuals']:
		if individual['alive'] == True and ((individual['birthday'].month == datetime.datetime.now().month) or (individual['birthday'].month -1 == datetime.datetime.now().month and individual['birthday'].day < datetime.datetime.now().day)):
				print("INFO: INDIVIDUAL: US38: " + info['individuals']['id'] + " has a birthday coming up")
				ret += 1
	return ret