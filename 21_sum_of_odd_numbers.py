'''
# Sum of odd numbers

ex. 
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

row sums of triangle from the row index, ex.
row_sum_odd_numbers(1) --> 1
row_sum_odd_numbers(2) --> 8 (3+5)
'''

def row_sum_odd_numbers(n):
	return sum(list(range(1, 2*sum(range(n+1)), 2))[-n:])

