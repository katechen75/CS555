# Author(s):  Matt Dimaculangan, Kurt von Autenried

# Code for User Story 1

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

class dates_before_current:
	def __init__(self):
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

class test_dates_before_current(unittest.TestCase):
	def make_test_file(self, file_name):
		#to implement
		return

	def check_output(self, check_value):
		capturedOutput = StringIO()
		sys.stdout = capturedOutput
		dates_before_current()
		sys.stdout = sys.__stdout__
		self.assertIn(check_value, capturedOutput.getvalue())

	#@patch.object(sys, 'argv', ['us01.py','test_birthday.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_indi_birthday(self):
		check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday 10-30-2022 occurs in the future'
		self.check_output(check_value)

	#@patch.object(sys, 'argv', ['us01.py','test_birthday_exists.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_indi_birthday_exists(self):
		check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday does not exist'
		self.check_output(check_value)

	#@patch.object(sys, 'argv', ['us01.py','test_death.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_indi_death(self):
		check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Death 10-30-2022 occurs in the future'
		self.check_output(check_value)

	#@patch.object(sys, 'argv', ['us01.py','test_married.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_fam_married(self):
		check_value = 'ERROR: FAMILY: US01: @F1@: Married 10-30-2022 occurs in the future'
		self.check_output(check_value)

	#@patch.object(sys, 'argv', ['us01.py','test_married_exists.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_fam_married_exists(self):
		check_value = 'ERROR: FAMILY: US01: @F8@: Married date does not exist'
		self.check_output(check_value)

	#@patch.object(sys, 'argv', ['us01.py','test_divorce.ged'])
	@patch.object(sys, 'argv', ['us01.py','kurt_project01.ged'])
	def test_fam_divorce(self):
		check_value = 'ERROR: FAMILY: US01: @F1@: Divorce 10-30-2022 occurs in the future'
		self.check_output(check_value)



if __name__ == '__main__':
	dates_before_current()
	unittest.main(argv=[sys.argv[0]])

