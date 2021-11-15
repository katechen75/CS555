# Author: Kurt von Autenried

# Code for User Story 24

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def unique_family_by_spouse():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for family1 in range(0, len(info['families'])):
		for family2 in range(1, len(info['families'])):
			if info['families'][family1]['married'] == info['families'][family2]['married'] and \
			(info['families'][family1]['wife_id'] == info['families'][family2]['wife_id'] or \
				info['families'][family1]['husband_id'] == info['families'][family2]['husband_id']):
				ret += 1
				print("ERROR: FAMILY: US24: " + info['families'][family1]['id'] + ", " + info['families'][family2]['id'] + " have the same spouse and marriage date")
	return ret