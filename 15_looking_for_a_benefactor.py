'''
Looking for a benefactor

ex. 
dons = [14,30,5,7,9,11,15] --> new_avg(dons, 30)=149
'''

import math

def new_avg(arr, newavg):
    nextDonat = newavg * (len(arr) + 1) - sum(arr)
    
    if nextDonat < 0:
        raise ValueError
    return math.ceil(nextDonat)