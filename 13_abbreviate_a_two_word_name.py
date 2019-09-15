'''
Abbreviate a Two Word Name

ex. 
Sam Harris --> S.H
Patrick Feeney --> P.F
'''

def abbrevName(name):
	return '.'.join([x[0].upper() for x in name.split(' ')])


