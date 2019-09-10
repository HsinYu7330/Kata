'''
# Easy Line

Calculate the sum of the squares of the binomial coefficients on a given line with a function called easyline
'''

import math

def easyline(n):
	binomial_coef = [(math.factorial(n)//(math.factorial(i)*math.factorial(n-i)))**2 for i in range(n+1)]

	return int(sum(binomial_coef))

