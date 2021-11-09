from project03 import *
import sys

def male_last_name():
    file_name = sys.argv[1]
    info = get_info(file_name)
    each_fam_males = []
    for ind in info['individuals']:
        if ind['sex'] == 'M' and ind['child'] != None:
            each_fam_males.append({'male': ind['name'], 'famID': ind['child']})
            
    # reformat each fam male to just male last names
    for e in each_fam_males:
        e['male'] = e['male'].rsplit('/', 2)[1]

    # compare fam id to male
    for index1 in range(0, len(each_fam_males)):
        for index2 in range(1, len(each_fam_males)):
            if (each_fam_males[index1]['famID'] == each_fam_males[index2]['famID'] and each_fam_males[index1]['male'] != each_fam_males[index2]['male']):
                print('US16 ERROR: male last names are not the same')
                return 1
                 
    return 0

male_last_name()
if __name__ == '__main__':
    male_last_name()
    