
from project03 import *
import sys
from unittest.mock import patch
from io import StringIO

def corect_gender():
    file_name = sys.argv[1]
    info = get_info(file_name)
    ret = 0
    for family in info['families']:	
        husband_ids = []
        wife_ids = []
        for individual in info['individuals']:
            if individual["id"] in family['husband_id']:
                husband_ids.append({"id": individual["id"]})
            if individual["id"] in family['wife_id']:
                wife_ids.append({"id": individual["id"]})
            for husband in husband_ids:
                if (husband["id"] == individual["id"] and individual["sex"]=="F"):
                    print("ERROR: FAMILY: US21: " + individual["id"] + "Husband cannot be female")
                    ret += 1
            for wife in wife_ids:
                if (wife["id"] == individual["id"] and individual["sex"]=="M"):
                    print("ERROR: FAMILY: US21: " + individual["id"] + "Wife cannot be female")
                    ret += 1
    return ret

if __name__ == "__main__":
    corect_gender()