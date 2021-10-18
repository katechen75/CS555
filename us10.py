# Author(s): Taylor Niedzielski
# Code for User Story 10: Marriage after 14
from project03 import *
import sys
import datetime
import unittest

file_name = sys.argv[1]
info = get_info(file_name)

def marriageAfter14():
    for family in info['families']:	
        if family['married'] != None:
            married = family['married'].split(" ")
            mday = int(married[0])
            mmonth = month_to_num[married[1]]
            myear = int(married[2])
            m = datetime.datetime(myear, mmonth, mday)
            wbirth = None
            hbirth = None
            for individual in info['individuals']:
                if individual["id"] == family['wife_id']:
                    wbirth = individual['birthday']
                    #check if woman is 14
                    daysBeforeMarriage = (m - wbirth).days
                    if (daysBeforeMarriage < ((14*365)+4) ): 
                        print("ERROR: INDIVIDUAL: US10: " + individual['id'] + " younger than 14 when married. " + " Birthday: " + wbirth.strftime("%m-%d-%Y") + "  Married: " + m.strftime("%m-%d-%Y"))
                        return False
                elif individual["id"] == family['husband_id']:
                    hbirth = individual['birthday']
                    daysBeforeMarriage = (m - hbirth).days
                    if (daysBeforeMarriage < ((14*365)+4) ): 
                        print("ERROR: INDIVIDUAL: US10: " + individual['id'] + " younger than 14 when married. " + " Birthday: " + hbirth.strftime("%m-%d-%Y") + "  Married: " + m.strftime("%m-%d-%Y"))
                        return False
                else:
                    return True
            

