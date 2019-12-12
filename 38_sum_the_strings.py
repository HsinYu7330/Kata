'''
Sum The Strings

ex. 
('4', '5') --> '9'
'''

def sum_str(a, b):
	return str(sum(int(x) for x in (a, b) if len(x) != 0))

