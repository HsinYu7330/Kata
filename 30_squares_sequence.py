'''
Squares sequence

ex. 
(x, n)
(2, 5) --> [2, 4, 16, 256, 65536]
(3, 3) --> [3, 9, 81]
'''

def squares(x, n):

	if n <= 0:
		return []
	else:
		arr = []
		arr.append(x)
		while len(arr) < n:
			arr.append(arr[-1]**2)
		return arr



