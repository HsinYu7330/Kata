'''
Next smaller number with the same digits
(Execution Timed Out)

ex. 
21 --> 12
531 --> 513
135 --> -1
'''

from itertools import permutations

def next_smaller(n):
	
	n = str(n)

	for i in range(len(n)-1):
		if n[i] > n[i+1]:
			ix = i
			break

	try:
		next_smaller_number = n[:ix] + max([''.join(x) for x in list(permutations(n[ix:])) if int(''.join(x)) < int(n[ix:])])
		if next_smaller_number[0] == '0':
			return -1
		else:
			return int(next_smaller_number) 
	except:
		return -1


n = 1234567908

print(next_smaller(n))
