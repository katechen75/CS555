# Author(s):  Matt Dimaculangan, Kurt von Autenried

# Code for User Story 1

# 2 bad smells:

# 1) Duplicated code on converting string dates to datetime

# 2) Turn datetime.datetime.now() fragment into variable

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

test_file_name="test.ged"
test_married=1
test_married_exists=2
test_divorce=3
test_death=4
test_birthday=5
test_birthday_exists=6

def convert_string_to_datetime(date_string):
	string_dmy = date_string.split(" ")
	string_day = int(string_dmy[0])
	string_month = month_to_num[string_dmy[1]]
	string_year = int(string_dmy[2])
	return datetime.datetime(string_year, string_month, string_day)

class dates_before_current:
    def __init__(self):
        file_name = sys.argv[1]
        info = get_info(file_name)

        now = datetime.datetime.now()

        for individual in info['individuals']:
            if individual['birthday'] != None:
                if individual['birthday'] > now:
                    print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Birthday " + individual['birthday'].strftime("%m-%d-%Y") + " occurs in the future")
            else:
                print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Birthday does not exist")        
            if individual['death'] != None:
                if individual['death'] > now:
                    print("ERROR: INDIVIDUAL: US01: " + individual['id'] + ": Death " + individual['death'].strftime("%m-%d-%Y") + " occurs in the future")

        for family in info['families']:
            if family['married'] != None:
                m = convert_string_to_datetime(family['married'])
                if m > now:
                    print("ERROR: FAMILY: US01: " + family['id'] + ": Married " + m.strftime("%m-%d-%Y") + " occurs in the future")
            else:
                print("ERROR: FAMILY: US01: " + family['id'] + ": Married date does not exist")        
            if family['divorced'] != None:
                d = convert_string_to_datetime(family['divorced'])
                if d > now:
                    print("ERROR: FAMILY: US01: " + family['id'] + ": Divorce " + d.strftime("%m-%d-%Y") + " occurs in the future")

class test_dates_before_current(unittest.TestCase):
    def make_test_file(self, test_type):
        #to implement, should be done with case based on test_type
        f = open(test_file_name,"w")
        if test_type == test_birthday:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 SEX M\n1 BIRT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 TRLR\n", file=f)
        if test_type == test_birthday_exists:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 SEX M\n1 FAMC @F1@\n0 TRLR\n", file=f)
        if test_type == test_divorce:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 2022\n0 TRLR\n", file=f)
        if test_type == test_married:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 2022\n1 DIV\n2 DATE 30 OCT 1999\n0 TRLR\n", file=f)
        if test_type == test_married_exists:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 DIV\n2 DATE 30 OCT 1998\n0 TRLR\n", file=f)
        if test_type == test_death:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 DEAT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 1999\n0 TRLR\n", file=f)
        f.close()
        return

    def check_output(self, check_value):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        dates_before_current()
        sys.stdout = sys.__stdout__
        self.assertIn(check_value, capturedOutput.getvalue())

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_birthday(self):
        self.make_test_file(test_birthday)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_birthday_exists(self):
        self.make_test_file(test_birthday_exists)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday does not exist'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_death(self):
        self.make_test_file(test_death)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Death 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_married(self):
        self.make_test_file(test_married)
        check_value = 'ERROR: FAMILY: US01: @F1@: Married 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_married_exists(self):
        self.make_test_file(test_married_exists)
        check_value = 'ERROR: FAMILY: US01: @F1@: Married date does not exist'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_divorce(self):
        self.make_test_file(test_divorce)
        check_value = 'ERROR: FAMILY: US01: @F1@: Divorce 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)



if __name__ == '__main__':
    dates_before_current()
    unittest.main(argv=[sys.argv[0]])

