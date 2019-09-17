'''
Primorial Of a Number

ex. 
3 --> 30 (2*3*5=30)
5 --> 2310 (2*3*5*7*9)
'''

from functools import reduce

def num_primorial(n):
	
	prime = []
	start = 2
	while len(prime) < n:
		for k in range(2, start):
			if start % k == 0: # not a prime nummber
				break
		else:
			prime.append(start)
		start += 1

	return reduce((lambda x, y: x*y), prime)


