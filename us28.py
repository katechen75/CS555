## all individuals id should be different as well as birthdays
## all the family id shoud be unique
from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO


def unique_ids():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for family1 in range(0, len(info['families'])):
		for family2 in range(1, len(info['families'])):
			if family1[id] == family2['families'][id]:
				print("ERROR: FAMILY: US28: " + family1['id'] + ", " + family2['id'] + " have the same id")
                ret = 1
	for ind1 in range(0, len(info['individuals'])):
		for ind2 in range(1, len(info['individuals'])):
            if (ind1['id'] == ind2['id']) & (ind1['birthday'] == ind2['birthday']):
				print("ERROR: FAMILY: US28: " + ind1['id'] + ", " + ind2['id'] + " have the same id and birthday")
                ret =1
    return ret


