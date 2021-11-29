# Matthew Dimaculangan
# CS 555 - User Story 36

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def recent_deaths():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    for individual in info['individuals']:
        if individual['death'] is not None:
            current_deathdate = datetime.date(individual['death'].year, individual['death'].month, individual['death'].day)
            if ((datetime.date.today() - current_deathdate).days <= 30):
                    print("INFO: INDIVIDUAL: US36: " + individual['id'] + " passed away within the last 30 days.")
                    ret += 1
    return ret

if __name__ == "__main__":
    recent_deaths()