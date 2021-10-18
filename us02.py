# Author(s):  Katelyn Chen and Taylor Niedzielski
# Code for User Story 2: Birth before marriage

from project03 import *
import sys
import datetime
import unittest

file_name = sys.argv[1]
info = get_info(file_name)

def formatMarriedDate(date):
    married = date.split(" ")
    mday = int(married[0])
    mmonth = month_to_num[married[1]]
    myear = int(married[2])
    m = datetime.datetime(myear, mmonth, mday)
    return m

def birthBeforeMarriage():
    def __init__(self):
        for family in info['families']:	
            if family['married'] != None:
                # fixed smelly code
                m = formatMarriedDate(family['married'])
                wbirth = None
                hbirth = None
                for individual in info['individuals']:
                    if individual["id"] == family['wife_id']:
                        wbirth = individual['birthday']
                    elif individual["id"] == family['husband_id']:
                        hbirth = individual['birthday']

                if hbirth != None and wbirth != None:
                    if (hbirth > m) or (wbirth > m):
                        return print("ERROR: FAMILY: US02: " + family['id'] + ": Marriage " + m.strftime("%m-%d-%Y") + " occurs before birthdays of both spouses")

#print(formatMarriedDate('3 JAN 1957'))

