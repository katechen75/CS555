# Author:  Kurt von Autenried

# Code for User Story 12

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def parents_not_too_old():
	file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
	for family in info['families']:	
		husband_birth = None
		wife_birth = None
		children_births = []
		for individual in info['individuals']:
			if individual["id"] == family['wife_id']:
				wife_birth = individual['birth']
			if individual["id"] == family['husband_id']:
				husband_birth = individual['birth']
			if individual["id"] in family['children']:
				children_births.append({"id": individual["id"], "birth": individual["birth"]})
		for child in children_births:
			if husband_birth != None:
				if (child["birth"].year - husband_birth.year > 80) or (child["birth"].year - husband_birth.year == 80 and child["birth"].month > husband_birth.month) or (child["birth"].year - husband_birth.year == 80 and child["birth"].month == husband_birth.month and child["birth"].day > husband_birth.month):
					ret += 1
					print("ERROR: FAMILY: US12: " + child["id"] + ": Birthday " + child['birthday'].strftime("%m-%d-%Y") + " occurs more than 80 days after father")
			if wife_birth != None:
				if (child["birth"].year - husband_birth.year > 60) or (child["birth"].year - husband_birth.year == 60 and child["birth"].month > husband_birth.month) or (child["birth"].year - husband_birth.year == 60 and child["birth"].month == husband_birth.month and child["birth"].day > husband_birth.month):
					ret += 1
					print("ERROR: FAMILY: US12: " + child["id"] + ": Birthday " + child['birthday'].strftime("%m-%d-%Y") + " occurs more than 60 days after mother")
	return ret