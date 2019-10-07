'''
Unique In Order

ex. 
'AAAABBBCCDAABBB' --> ['A', 'B', 'C', 'D', 'A', 'B']
'ABBCcAD' --> ['A', 'B', 'C', 'c', 'A', 'D']
[1,2,2,3,3] --> [1,2,3]
'''

def unique_in_order(iterable):

	uniArr = []
	if len(iterable) == 0:
		return uniArr
	else:
		uniArr.append(iterable[0])
		for i in range(1, len(iterable)):
			if iterable[i] != iterable[i-1]:
				uniArr.append(iterable[i])
		return uniArr

