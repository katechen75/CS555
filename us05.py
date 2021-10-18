# Author:  Matthew Dimaculangan

# Code for User Story 5

from project03 import *
import sys
import datetime
import unittest

file_name = sys.argv[1]
info = get_info(file_name)

isError = False

def marriageBeforeDeath():
	for family in info['families']:	
		if family['married'] != None:
			marriage_dmy = family['married'].split(" ")
			marriage_day = int(marriage_dmy[0])
			marriage_month = month_to_num[marriage_dmy[1]]
			marriage_year = int(marriage_dmy[2])
			d = datetime.datetime(marriage_year, marriage_month, marriage_day)
			husband_death = None
			wife_death = None
			for individual in info['individuals']:
				if individual["id"] == family['wife_id']:
					wife_death = individual['death']
				elif individual["id"] == family['husband_id']:
					husband_death = individual['death']
			if husband_death != None and wife_death != None:
				if husband_death < d and wife_death < d:
					print("ERROR: FAMILY: US05: " + family['id'] + ": Married " + d.strftime("%m-%d-%Y") + " occurs after death of both spouses" + " Husband Death: " + str(husband_death) + " Wife Death " + str(wife_death))
					isError = True
	return isError

class Testing(unittest.TestCase):
    print('test 1: marriage before death - assertEqual')
    def test_marriedFam(self):
        self.assertTrue(marriageBeforeDeath(), True)

    print('test 1: marriage before death - assertFalse')
    def test_marriedFam2(self):
        self.assertTrue(marriageBeforeDeath(), False)


  
if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])