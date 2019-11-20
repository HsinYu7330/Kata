'''
Count the divisible numbers

ex. 
x = 6, y = 11, k = 2 --> 3
because there are three numbers divisible by 2 between 6 and 11
'''

def divisible_count(x, y, k):

	a = x//k
	b = y//k

	if x%k == 0:
		return b-a+1
	else:
		return b-a
