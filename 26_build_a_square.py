'''
Build a square

ex. 
n = 3 --> 
+++
+++
+++
'''

def generateShape(int):
    return '\n'.join(['+'*int]*int)