'''
# Century From Year
ex. 
1705 --> 18
1900 --> 19
1601 --> 17
'''

import math

def century(year):
	return math.ceil(year/100)

