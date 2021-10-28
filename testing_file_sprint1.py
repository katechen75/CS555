## testing file

from us06 import *
from us07 import *
from us10 import *
from us01 import *
from us02 import *
import unittest
from unittest.mock import patch
from io import StringIO
import sys

## user story 1
test_file_name="test.ged"
test_married=1
test_married_exists=2
test_divorce=3
test_death=4
test_birthday=5
test_birthday_exists=6



class test_dates_before_current(unittest.TestCase):
    def make_test_file(self, test_type):
        #to implement, should be done with case based on test_type
        f = open(test_file_name,"w")
        if test_type == test_birthday:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 SEX M\n1 BIRT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 TRLR\n", file=f)
        if test_type == test_birthday_exists:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 SEX M\n1 FAMC @F1@\n0 TRLR\n", file=f)
        if test_type == test_divorce:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 2022\n0 TRLR\n", file=f)
        if test_type == test_married:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 2022\n1 DIV\n2 DATE 30 OCT 1999\n0 TRLR\n", file=f)
        if test_type == test_married_exists:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 DIV\n2 DATE 30 OCT 1998\n0 TRLR\n", file=f)
        if test_type == test_death:
            print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 DEAT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 FAMC @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 1999\n0 TRLR\n", file=f)
        f.close()
        return

    def check_output(self, check_value):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        dates_before_current()
        sys.stdout = sys.__stdout__
        self.assertIn(check_value, capturedOutput.getvalue())

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_birthday(self):
        self.make_test_file(test_birthday)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_birthday_exists(self):
        self.make_test_file(test_birthday_exists)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Birthday does not exist'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_indi_death(self):
        self.make_test_file(test_death)
        check_value = 'ERROR: INDIVIDUAL: US01: @I1@: Death 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_married(self):
        self.make_test_file(test_married)
        check_value = 'ERROR: FAMILY: US01: @F1@: Married 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_married_exists(self):
        self.make_test_file(test_married_exists)
        check_value = 'ERROR: FAMILY: US01: @F1@: Married date does not exist'
        self.check_output(check_value)
        os.remove(test_file_name)

    @patch.object(sys, 'argv', ['us01.py',test_file_name])
    def test_fam_divorce(self):
        self.make_test_file(test_divorce)
        check_value = 'ERROR: FAMILY: US01: @F1@: Divorce 10-30-2022 occurs in the future'
        self.check_output(check_value)
        os.remove(test_file_name)


## User story 2
class Testing(unittest.TestCase):
    def test_marriedFam(self):
        self.assertNotEqual(birthBeforeMarriage(), 123)

    def test_marriedFam1(self):
        self.assertNotEqual(birthBeforeMarriage(), int('19570401'))

## user story 6
class test_divorce_before_death(unittest.TestCase):
    def make_test_file(self):
        #to implement, should be done with case based on test_type
        f = open(test_file_name,"w")
        print("0 HEAD\n1 GEDC\n0 @I1@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 DEAT\n2 DATE 30 OCT 2022\n1 FAMC @F1@\n0 @I2@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1998\n1 FAMC @F1@\n0 @I3@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 DEAT\n2 DATE 30 OCT 2012\n1 FAMS @F1@\n0 @I4@ INDI\n1 NAME John Smith\n2 GIVN John\n2 SURN Smith\n1 BIRT\n2 DATE 30 OCT 1968\n1 DEAT\n2 DATE 30 OCT 2015\n1 FAMS @F1@\n0 @F1@ FAM\n1 HUSB @I3@\n1 WIFE @I4@\n1 CHIL @I1@\n1 CHIL @I2@\n1 MARR\n2 DATE 30 OCT 1998\n1 DIV\n2 DATE 30 OCT 2020\n0 TRLR\n", file=f)
        f.close()
        return

    def check_output(self, check_value):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        divorce_before_death()
        sys.stdout = sys.__stdout__
        self.assertIn(check_value, capturedOutput.getvalue())

    @patch.object(sys, 'argv', ['us06.py',test_file_name])
    def test_both_deaths_after_divorce(self):
        self.make_test_file()
        check_value = 'ERROR: FAMILY: US06: @F1@: Divorce 10-30-2020 occurs after death of both spouses'
        self.check_output(check_value)
        os.remove(test_file_name)


if __name__ == '__main__':
    divorce_before_death()
    unittest.main(argv=[sys.argv[0]])


##user story 7
class Testing(unittest.TestCase):
    def test_youngerThan150a(self):
        self.assertTrue(lessThan150(), True)

    def test_youngerThan150b(self):
        self.assertTrue(lessThan150(), False)

## user stroy 10
class Testing(unittest.TestCase):
    def test_marriedFam(self):
        self.assertTrue(marriageAfter14(), True)

    print('test 2: marriage after 14 - assertFalse')
    def test_marriedFam2(self):
        self.assertTrue(marriageAfter14(), False)


  

if __name__ == '__main__':
    dates_before_current()
    unittest.main(argv=[sys.argv[0]])

