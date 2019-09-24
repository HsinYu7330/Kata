'''
Gap in Primes
(Execution Timed Out)

ex. 
gap(g(gap), m(start number), n(end number))
gap(2,100,110) --> [101, 103]
gap(4,100,110) --> [103, 107]
gap(6,100,110) --> None
'''

def gap(g, m, n):

	before = 0
	interval = [x for x in range(m, n+1) if x%2]
	for i in interval:
		for k in range(2, i):
			if i % k == 0: # not primes
				break
		else:
			if i - before == g:(Execution Timed Out)

				return [before, i]
			else:
				before = i