'''
Permutations

ex. 
'a' --> ['a']
'ab' --> ['ab', 'ba']
'''

from itertools import permutations as Permutation

def permutations(string):
	 return sorted([''.join(x) for x in list(set(Permutation(string, len(string))))])

