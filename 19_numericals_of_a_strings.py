'''
Numericals of a String

ex. 
'Hello, World!' --> 1112111121311
'aaaaaaaaaaaa' --> 123456789101112
'''

from collections import OrderedDict

def numericals(s):

	wordDict = OrderedDict()
	results = []

	for i in s:
		try:
			wordDict[i] += 1
		except:
			wordDict[i] = 1

		results.append(str(wordDict[i]))

	return ''.join(results)

