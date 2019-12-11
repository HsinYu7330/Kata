'''
Counting Duplicates
'''

from collections import Counter

def duplicate_count(text):
	
	text = text.lower()
	return len({char for char, cnt in Counter(text).items() if cnt>=2})


