from project03 import *
import sys
import operator

def order_sibs():
	file_name = sys.argv[1]
	info = get_info(file_name)
	sorted_sib = {}
	for fam in info['families']:
		# array of sib in each fam
		for child in fam['children']:
			for ind in info['individuals']:
				if ind['id'] == child:
					sorted_sib[child] = ind['birthday']
	if len(sorted_sib) == 0:
		return 1
	else:	
		ordered = dict( sorted(sorted_sib.items(), key = operator.itemgetter(1)))
		print(ordered.keys())
	return 0

if __name__ == '__main__':
	order_sibs()