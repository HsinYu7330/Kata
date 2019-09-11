'''
# Ordered Count of Characters

ex. 
'abracadabra' --> [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
'''

def ordered_count(input):
	return [(x, input.count(x)) for x in sorted(set(input), key=input.index)]


