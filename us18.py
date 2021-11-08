# Matthew Dimaculangan
# User Story 17 - No marriages to descendants

from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def no_marriages_to_siblings():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    children_births = []
    for individual in info['individuals']:
        if individual["child"] != None:
            children_births.append({"id": individual["child"]})
        for index1 in range(0, len(children_births)):
            for index2 in range(1, len(children_births)):
                for family in info['families']:
                    if (children_births[index1] == family['id']) and (children_births[index2] == family['id']):
                        print("Error US18: siblings cannot marry siblins")
                        ret = 1
                        
if __name__ == "__main__":
	no_marriages_to_siblings()
 