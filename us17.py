# Matthew Dimaculangan
# User Story 17 - No marriages to descendants

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def no_marriages_to_descendants():
	file_name = sys.argv[1]
	info = get_info(file_name)
	ret = 0
	for family in info['families']:	
		children_births = []
		for individual in info['individuals']:
			if individual["id"] in family['children']:
				children_births.append({"id": individual["id"]})
		for child in children_births:
			if (child["id"] == family["husband_id"]):
				print("ERROR: FAMILY: US17: " + child["id"] + " cannot be married to parent: " + family["husband_id"])
				ret += 1
			if (child["id"] == family["wife_id"]):
				print("ERROR: FAMILY: US17: " + child["id"] + " cannot be married to parent: " + family["wife_id"])
				ret += 1
	return ret

if __name__ == "__main__":
	no_marriages_to_descendants()