# Author: Kurt von Autenried

# Code for User Story 37

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def get_descendants(ind, fam, info, desc):
	if fam == None:
		return desc
	else:
		for individual in info['individuals']:
			if individual['id'] == fam['husband_id'] and fam['husband_id'] != ind['id'] and individual['alive'] == True:
				desc.append(individual['id'])
			elif individual['id'] == fam['wife_id'] and fam['wife_id'] != ind['id'] and individual['alive'] == True:
				desc.append(individual['id'])
			if individual['id'] in fam['children']:
				if individual['alive'] == True:
					desc.append(individual['id'])
				next_fam = None
				for family in info['families']:
					if family['id'] == individual['spouse']:
						next_fam = family
				desc += get_descendants(individual, next_fam, info, desc)
		return desc

def recent_survivors():
	file_name = sys.argv[1]
	info = get_info(file_name)
	survivors = []
	for family in info['families']:
		for individual in info['individuals']:
			if individual["id"] == family['wife_id']:
				if individual['alive'] == False and ((individual['death'].month == datetime.datetime.now().month) or (individual['death'].month + 1 == datetime.datetime.now().month and individual['death'].day >= datetime.datetime.now().day)):
					survivors += get_descendants(individual, family, info, [])	
			if individual["id"] == family['husband_id']:
				if individual['alive'] == False and ((individual['death'].month == datetime.datetime.now().month) or (individual['death'].month + 1 == datetime.datetime.now().month and individual['death'].day >= datetime.datetime.now().day)):
					survivors += get_descendants(individual, family, info, [])
	unique_vals = set(survivors)
	unique_list = []
	for val in unique_vals:
		unique_list.append(val)
	for person in unique_list:
		print("INFO: INDIVIDUAL: US37: " + person + " is a recent survivor")
	return len(unique_list)