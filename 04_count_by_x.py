'''
# Count by X

ex. 
count_by(1, 10) --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_by(2, 5) --> [2, 4, 6, 8, 10]
'''

def count_by(x, n):
	return [x*(k+1) for k in range(n)]

