# Author:  Kurt von Autenried

# Code for User Story 6

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO
import os

test_file_name="test.ged"

class divorce_before_death:
	def __init__(self):
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
					if individual["id"] == family['husband_id']:
						husband_death = individual['death']
				if husband_death != None and wife_death != None:
					if husband_death < d and wife_death < d:
						print("ERROR: FAMILY: US06: " + family['id'] + ": Divorce " + d.strftime("%m-%d-%Y") + " occurs after death of both spouses")


class test_divorce_before_death(unittest.TestCase):
    def make_test_file(self):
        #to implement, should be done with case based on test_type
        f = open(test_file_name,"w")
        print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 DEAT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 DEAT\n2 DATE 30 OCT 2012\n1 FAMS @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 DEAT\n2 DATE 30 OCT 2015\n1 FAMS @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 2020\n0 TRLR\n", file=f)
        f.close()
        return

    def check_output(self, check_value):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        divorce_before_death()
        sys.stdout = sys.__stdout__
        self.assertIn(check_value, capturedOutput.getvalue())

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_both_deaths_after_divorce(self):
        self.make_test_file()
        check_value = 'ERROR: FAMILY: US06: @F1@: Divorce 10-30-2020 occurs after death of both spouses'
        self.check_output(check_value)
        os.remove(test_file_name)


if __name__ == '__main__':
    divorce_before_death()
    unittest.main(argv=[sys.argv[0]])