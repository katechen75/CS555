# Author(s):  Matt Dimaculangan, Kurt von Autenried

# Code for User Story 1

from project03 import *
import sys
import datetime

file_name = sys.argv[1]
info = get_info(file_name)

for individual in info['individuals']:
	if individual['birthday'] != None:
		if individual['birthday'] > datetime.datetime.now():
			print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Birthday " + individual['birthday'].strftime("%m-%d-%Y") + " occurs in the future")
	else:
		print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Birthday does not exist")		
	if individual['death'] != None:
		if individual['death'] > datetime.datetime.now():
			print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Death " + individual['death'].strftime("%m-%d-%Y") + " occurs in the future")

for family in info['families']:
	if family['married'] != None:
		married_dmy = family['married'].split(" ")
		married_day = int(married_dmy[0])
		married_month = month_to_num[married_dmy[1]]
		married_year = int(married_dmy[2])
		m = datetime.datetime(married_year, married_month, married_day)
		if m > datetime.datetime.now():
			print("ERROR: FAMILY: US01: " + family['id'] + ": Married " + m.strftime("%m-%d-%Y") + " occurs in the future")
	else:
		print("ERROR: FAMILY: US01: " + family['id'] + ": Married date does not exist")		
	if family['divorced'] != None:
		divorce_dmy = family['divorced'].split(" ")
		divorce_day = int(divorce_dmy[0])
		divorce_month = month_to_num[divorce_dmy[1]]
		divorce_year = int(divorce_dmy[2])
		d = datetime.datetime(divorce_year, divorce_month, divorce_day)
		if d > datetime.datetime.now():
			print("ERROR: FAMILY: US01: " + family['id'] + ": Divorce " + d.strftime("%m-%d-%Y") + " occurs in the future")

