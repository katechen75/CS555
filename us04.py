# Author(s):  Matt Dimaculangan, Kurt von Autenried

# Code for User Story 4

from project03 import *
import sys
import datetime

file_name = sys.argv[1]
info = get_info(file_name)

for family in info['families']:
    if family['married'] != None and family['divorced'] != None:
        married_dmy = family['married'].split(" ")
        married_day = int(married_dmy[0])
        married_month = month_to_num[married_dmy[1]]
        married_year = int(married_dmy[2])
        m = datetime.datetime(married_year, married_month, married_day)
        divorce_dmy = family['divorced'].split(" ")
        divorce_day = int(divorce_dmy[0])
        divorce_month = month_to_num[divorce_dmy[1]]
        divorce_year = int(divorce_dmy[2])
        d = datetime.datetime(divorce_year, divorce_month, divorce_day)
        if m > d:
            print("ERROR: FAMILY: US04: " + family['id'] + ": Married " + m.strftime("%m-%d-%Y") + " occurs after Divorce " + d.strftime("%m-%d-%Y"))