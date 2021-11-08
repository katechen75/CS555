from project03 import *
import os
import sys
import datetime
import unittest
from unittest.mock import patch
from io import StringIO

def multiple_sib_born():
    file_name = sys.argv[1]
    info = get_info(file_name)
    count = 0
    total_sib_born = 0
    
    for family in info['families']:
        children_birth = []
        for ind in info['individuals']:
            if (ind['id'] in family['children']):
                children_birth.append({'id': ind['id'], 'birth': ind['birthday']})
        for index1 in range(0, len(children_birth)):
            for index2 in range(1, len(children_birth)):
                timedelta = children_birth[index1]['birth'] - children_birth[index2]['birth']
                if(timedelta == 0):
                    total_sib_born += 1
    if(total_sib_born > 5):
        count += 1
        print('ERROR: US14: too many sibilings born at the same time')
    return count

if __name__ == '__main__':
    multiple_sib_born()
                