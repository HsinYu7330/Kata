'''
Invert values

ex. 
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
'''

def invert(lst):
	return [-x for x in lst]


