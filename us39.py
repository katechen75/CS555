## User story 39: list upcoming annniversaries
from project03 import *
from us30 import *
import sys
import datetime
from unittest.mock import patch
from io import StringIO

def list_upcoming_anniversaries():
    for fam in info['families']:	
        if fam['married'] != None:
            married = fam['married'].split(" ")
            mday = int(married[0])
            mmonth = month_to_num[married[1]]
            myear = int(married[2])
            m = datetime.datetime(myear, mmonth, mday)
            
            d = datetime.datetime.now() - m
            d = d % datetime.timedelta(days=365)
            ann = []
            if d.days < 30:
                ann.append(fam['id'])
                print(ann)
                return 1
    return 0

list_upcoming_anniversaries()