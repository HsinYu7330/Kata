'''
Maximum Multiple

Given a Divisor and a Bound, Find the largest integer N
ex. 
(2, 7) --> 6
(6) is divisible by (2), and is less than or equal to bound (7), and is > 0
'''

def max_multiple(divisor, bound):
    return divisor*(bound//divisor)



