'''
Bit Counting

ex. 
1234 --> 10011010010 --> 5
10 --> 1010 --> 2
'''

def countBits(n):
	return str(bin(n)[2:]).count('1')


