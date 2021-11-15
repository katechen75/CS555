# Author:  Kurt von Autenried

# Code for User Story 13

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def sibling_age_diff():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for family in info['families']:	
		children_births = []
		for individual in info['individuals']:
			if individual["id"] in family['children']:
				children_births.append({"id": individual["id"], "birth": individual["birthday"]})
		for index1 in range(0, len(children_births)):
			for index2 in range(index1 + 1, len(children_births)):
				timedelta = children_births[index1]["birth"] - children_births[index2]["birth"]
				if timedelta.total_seconds()/(60*60*24) > 2 and timedelta.total_seconds()/(60*60*24) < 30 * 8:
					print("ERROR: FAMILY: US12: " + children_births[index1]["id"] + ": Birthday " + children_births[index1]['birth'].strftime("%m-%d-%Y") + " occurs too close to birthday of " + children_births[index2]["id"])
					ret += 1
	return ret