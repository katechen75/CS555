# Author:  Kurt von Autenried

# Code for User Story 6

from project03 import *
import sys
import datetime

file_name = sys.argv[1]
info = get_info(file_name)

for family in info['families']:	
	if family['divorced'] != None:
		divorce_dmy = family['divorced'].split(" ")
		divorce_day = int(divorce_dmy[0])
		divorce_month = month_to_num[divorce_dmy[1]]
		divorce_year = int(divorce_dmy[2])
		d = datetime.datetime(divorce_year, divorce_month, divorce_day)
		husband_death = None
		wife_death = None
		for individual in info['individuals']:
			if individual["id"] == family['wife_id']:
				wife_death = individual['death']
			elif individual["id"] == family['husband_id']:
				husband_death = individual['death']
		if husband_death != None and wife_death != None:
			if husband_death < d and wife_death < d:
				print("ERROR: FAMILY: US01: " + family['id'] + ": Divorce " + d.strftime("%m-%d-%Y") + " occurs after death of both spouses")

