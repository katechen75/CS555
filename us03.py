# Author(s):  Katelyn Chen and Taylor Niedzielski
# Code for User Story 3: Birth before death

from project03 import *
import sys
import datetime

file_name = sys.argv[1]
info = get_info(file_name)

for ind in info['individuals']:
    if ind['birthday'] != None and ind['death'] != None:
        birth = ind['birthday']
        death = ind['death']
        if birth > death:
            print("ERROR: INDIVIDUAL: US03: " + ind['id'] + ": Birthday " + birth.strftime("%m-%d-%Y") + " occurs after Death " + death.strftime("%m-%d-%Y"))