'''
Form The Largest

ex. 
213 --> 321
7389--> 9873
'''

def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))