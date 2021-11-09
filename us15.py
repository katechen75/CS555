from project03 import *
import sys

def fewer_than_15_sib():
    file_name = sys.argv[1]
    info = get_info(file_name)
    fam_children = []
    for fam in info['families']:
        fam_children.append(fam['children'])
        
    for child in fam_children:
        if len(child) > 1:
            print("US15 ERROR: can not have more than 15 sibilings")
            return 1
        
    return 0

if __name__ == '__main__':
    fewer_than_15_sib()
    