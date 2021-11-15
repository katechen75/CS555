# Author: Kurt von Autenried

# Code for User Story 25

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def unique_child():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for family in info['families']:	
		children_info = []
		for individual in info['individuals']:
			if individual["id"] in family['children']:
				children_info.append({"id": individual["id"], "name": individual["name"], "birth": individual["birthday"]})
		for index1 in range(0, len(children_info)):
			for index2 in range(index1 + 1, len(children_info)):
				if children_info[index1]["name"] == children_info[index2]["name"] and children_info[index1]["birth"] == children_info[index2]["birth"]:
					ret += 1
					print("ERROR: FAMILY: US25: " + family['id'] + ": Children " + children_info[index1]['id'] + " and " + children_info[index2]["id"] + " have same name and birthday")
	return ret