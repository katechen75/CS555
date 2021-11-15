# Matthew Dimaculangan
# User Story 27 - Include individual ages

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def include_individual_ages():
    file_name = sys.argv[1]
    info = get_info(file_name)
    print(info)
    ret = 0
    for individual in info['individuals']:	
        print(str(individual['name']) + " age: " + str(individual['age']))
        ret += 1
    return ret

if __name__ == "__main__":
    include_individual_ages()