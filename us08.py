# Matthew Dimaculangan
# User Story 8 - Birth before marriage of parents

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def formatMarriedDate(date):
    married = date.split(" ")
    mday = int(married[0])
    mmonth = month_to_num[married[1]]
    myear = int(married[2])
    m = datetime.datetime(myear, mmonth, mday)
    return m

def birth_before_marriage():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    for family in info['families']:
        children_births = []
        if(family["married"] != None):
            married_date = formatMarriedDate(family["married"])
            for individual in info['individuals']:
                if individual["id"] in family['children']:
                    children_births.append({"id": individual["id"], "birth": individual["birthday"]})
            if (len(children_births) > 0):
                for child in children_births:
                    child_birth_str = str(child["birth"])
                    child_birth_y = int(child_birth_str[0:4])
                    child_birth_m = int(child_birth_str[5:7])
                    child_birth_d = int(child_birth_str[8:10])
                    child_birth = datetime.datetime(year=child_birth_y, month=child_birth_m, day=child_birth_d)
                    if (child_birth < married_date):
                        print("ERROR: FAMILY: US08: " + child["id"] + ": Birthday " + child['birth'].strftime("%m-%d-%Y") + " occurs before parents' " + family["id"] + " marriage " + married_date.strftime("%m-%d-%Y"))
                        ret += 1
    return ret

if __name__ == "__main__":
    birth_before_marriage()