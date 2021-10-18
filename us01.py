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

def dates_before_current():
   # def __init__(self):
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

