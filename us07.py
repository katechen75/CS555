# Author(s): Taylor Niedzielski
# Code for User Story 7: Less than 150 years old

from project03 import *
import sys
import unittest

file_name = sys.argv[1]
info = get_info(file_name)

def lessThan150():
    for ind in info['individuals']:
        if ind['birthday'] != None and ind['death'] != None:
            birth = ind['birthday']
            death = ind['death']
            aliveDays = (death - birth).days
            if (aliveDays > (150*365)+36):
                print("ERROR: INDIVIDUAL: US07: " + ind['id'] + " older than 150 years. " + " Birthday: " + birth.strftime("%m-%d-%Y") + "  Death: " + death.strftime("%m-%d-%Y"))
                return False
            else:
                return True


