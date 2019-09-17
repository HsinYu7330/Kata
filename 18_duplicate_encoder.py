'''
Duplicate Encoder

ex. 
'din' --> '((('
'recede' --> '()()()'
'''

def duplicate_encode(word):
	encoder = [')' if word.upper().count(x) > 1 else '(' for x in word.upper()]
	
	return ''.join(encoder)

