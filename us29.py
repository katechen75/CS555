# Matthew Dimaculangan
# User Story 29 - List deceased

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def list_deceased():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    for individual in info['individuals']:	
        if individual['death'] is not None:
            print(str(individual['name']) + " Death date: " + str(individual['death']))
            ret += 1
    return ret

if __name__ == "__main__":
    list_deceased()