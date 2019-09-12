'''
Find The Parity Outlier

ex. 
[2, 4, 0, 100, 4, 11, 2602, 36] --> 11
11 is the only odd number
'''

def find_outlier(integers):

	remainder = [divmod(x, 2)[1] for x in integers]

	if remainder.count(1) > remainder.count(0):
		return [x for x in integers if divmod(x, 2)[1] == 0][0]
	else:
		return [x for x in integers if divmod(x, 2)[1] == 1][0]


