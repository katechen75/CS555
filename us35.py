# Matthew Dimaculangan
# CS 555 - User Story 35

from project03 import *
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def recent_births():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    for individual in info['individuals']:
        current_birthdate = datetime.date(individual['birthday'].year, individual['birthday'].month, individual['birthday'].day)
        if ((datetime.date.today() - current_birthdate).days <= 30):
                print("INFO: INDIVIDUAL: US35: " + individual['id'] + " was born within the last 30 days.")
                ret += 1
    return ret

if __name__ == "__main__":
    recent_births()